# Copyright (c) 2013-2019 GitHub Inc.
# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import json
import os
import subprocess
import sys

basedir = os.path.dirname(__file__)
sys.path.append(os.path.join(basedir, os.pardir, 'node', 'tools'))
import install

def LoadPythonDictionary(path):
  file_string = open(path).read()
  try:
    file_data = eval(file_string, {'__builtins__': None}, None)
  except SyntaxError, e:
    e.filename = path
    raise
  except Exception, e:
    raise Exception('Unexpected error while reading %s: %s' % (path, str(e)))

  assert isinstance(file_data, dict), '%s does not eval to a dictionary' % path

  return file_data


FILENAMES_JSON_HEADER = '''
// This file is automatically generated by generate_gn_filenames_json.py
// DO NOT EDIT
'''.lstrip()

def RedirectV8(list):
  return [f.replace('deps/v8/', '../v8/', 1) for f in list]

def GitLsFiles(path, prefix):
  output = subprocess.check_output(['git', 'ls-files'], cwd=path)
  return [prefix + x for x in output.splitlines()]

if __name__ == '__main__':
  # Set up paths.
  root_dir = sys.argv[1]
  node_dir = os.path.join(root_dir, 'node')
  node_gyp_file = os.path.join(node_dir, 'node.gyp')
  inspector_gyp_file = os.path.join(node_dir,
      'src', 'inspector', 'node_inspector.gypi')
  openssl_gyp_file = os.path.join(node_dir,
      'deps', 'openssl', 'config', 'archs',
      'linux-x86_64', 'no-asm', 'openssl.gypi')
  out = {}
  # Load file lists from gyp files.
  node_gyp = LoadPythonDictionary(node_gyp_file)
  inspector_gyp = LoadPythonDictionary(inspector_gyp_file)
  openssl_gyp = LoadPythonDictionary(openssl_gyp_file)
  # Find JS lib file and single out files from V8.
  library_files = node_gyp['variables']['library_files']
  out['v8_library_files'] = [
      f.replace('deps/', '../') for f in library_files if f.startswith('deps/v8')]
  out['node_library_files'] = [
      f for f in library_files if not f.startswith('deps/v8')]
  out['all_library_files'] = library_files

  # Find C++ source files.
  node_lib_target = next(
      t for t in node_gyp['targets']
      if t['target_name'] == '<(node_lib_target_name)')
  node_source_blacklist = {
      '<@(library_files)',
      'common.gypi',
      '<(SHARED_INTERMEDIATE_DIR)/node_javascript.cc',
  }
  node_sources = [
      f for f in node_lib_target['sources']
      if f not in node_source_blacklist]
  out['node_sources'] = [
      f.replace('deps/v8/', '../v8/', 1) for f in node_sources]

  # Find cctest files.
  cctest_target = next(
      t for t in node_gyp['targets']
      if t['target_name'] == 'cctest')
  out['cctest_sources'] = cctest_target['sources']

  # Find inspector sources.
  inspector_sources = inspector_gyp['sources']
  out['inspector_sources'] = inspector_sources

  # Find OpenSSL sources.
  openssl_sources = openssl_gyp['variables']['openssl_sources']
  out['openssl_sources'] = openssl_sources
  # Find node/tools/doc content.
  tools_doc_dir = os.path.join(node_dir, 'tools', 'doc')
  out['tools_doc_files'] = GitLsFiles(tools_doc_dir, '//node/tools/doc/')

  # Find node/test/addons content.
  test_addons_dir = os.path.join(node_dir, 'test', 'addons')
  out['test_addons_files'] = GitLsFiles(test_addons_dir, '//node/test/addons/')

  # Find node/test/node-api content.
  test_node_api_dir = os.path.join(node_dir, 'test', 'node-api')
  out['test_node_api_files'] = GitLsFiles(test_node_api_dir,
                                          '//node/test/node-api/')
  # Find node/test/js-native-api content.
  test_js_native_api_dir = os.path.join(node_dir, 'test', 'js-native-api')
  out['test_js_native_api_files'] = GitLsFiles(test_js_native_api_dir,
                                               '//node/test/js-native-api/')

  # Find v8/include content.
  v8_include_dir = os.path.join(root_dir, 'v8', 'include')
  out['v8_headers'] = GitLsFiles(v8_include_dir, '//v8/include/')

  # Write file list as JSON.
  print(json.dumps(out, sort_keys=True, indent=2, separators=(',', ': ')))
