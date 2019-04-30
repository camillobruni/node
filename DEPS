# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

vars = {
  'build_revision': '5b91f2d38785680d33c532ecb1a853a03f3ad6af',
  'build_url': 'https://chromium.googlesource.com/chromium/src/build.git',

  'buildtools_revision': '3e50219fc4503f461b2176a9976891b28d80f9ab',
  'buildtools_url': 'https://chromium.googlesource.com/chromium/src/buildtools.git',

  'buildtools_clang_format_revision': '96636aa0e9f047f17447f2d45a094d0b59ed7917',
  'buildtools_clang_format_url': 'https://chromium.googlesource.com/chromium/llvm-project/cfe/tools/clang-format.git',

  'buildtools_libcxx_revision': '9b96c3dbd4e89c10d9fd8364da4b65f93c6f4276',
  'buildtools_libcxx_url': 'https://chromium.googlesource.com/chromium/llvm-project/libcxx.git',

  'buildtools_libcxxabi_revision': '0d529660e32d77d9111912d73f2c74fc5fa2a858',
  'buildtools_libcxxabi_url': 'https://chromium.googlesource.com/chromium/llvm-project/libcxxabi.git',

  'buildtools_libunwind_revision': '69d9b84cca8354117b9fe9705a4430d789ee599b',
  'buildtools_libunwind_url': 'https://chromium.googlesource.com/external/llvm.org/libunwind.git',

  'clang_revision': '3dd606a4e91b32c6f0116b38abac3ab0c4944ec3',
  'clang_url': 'https://chromium.googlesource.com/chromium/src/tools/clang.git',

  'depot_tools_revision': 'efe902b20b6ae0d367b354bdaa2e10c19349f880',
  'depot_tools_url': 'https://chromium.googlesource.com/chromium/tools/depot_tools.git',

  # GN CIPD package version.
  'gn_version': 'git_revision:64b846c96daeb3eaf08e26d8a84d8451c6cb712b',

  'googletest_revision': '8b6d3f9c4a774bef3081195d422993323b6bb2e0',
  'googletest_url': 'https://chromium.googlesource.com/external/github.com/google/googletest.git',

  'icu_revision': '4ae7482a0e9e1f77a793545d803086a5ad4bcfd8',
  'icu_url': 'https://chromium.googlesource.com/chromium/deps/icu.git',

  'jinja2_revision': 'b41863e42637544c2941b574c7877d3e1f663e25',
  'jinja2_url': 'https://chromium.googlesource.com/chromium/src/third_party/jinja2.git',

  'markupsafe_revision': '8f45f5cfa0009d2a70589bcda0349b8cb2b72783',
  'markupsafe_url': 'https://chromium.googlesource.com/chromium/src/third_party/markupsafe.git',

  'node_revision': 'e47157ba2a1e76f6c68050eaf665a218c611eb35',
  'node_url': 'https://chromium.googlesource.com/external/github.com/v8/node.git',

  'trace_common_revision' : '936ba8a963284a6b3737cf2f0474a7131073abee',
  'trace_common_url': 'https://chromium.googlesource.com/chromium/src/base/trace_event/common.git',

  'v8_revision': '19e9067826e2f40f30aef10f979c5f2199c601e9',
  'v8_url': 'https://chromium.googlesource.com/v8/v8.git',
}

deps = {
  'node-ci/base/trace_event/common': Var('trace_common_url') + '@' + Var('trace_common_revision'),
  'node-ci/build': Var('build_url') + '@' + Var('build_revision'),
  'node-ci/buildtools/clang_format/script': Var('buildtools_clang_format_url') + '@' + Var('buildtools_clang_format_revision'),
  'node-ci/buildtools/third_party/libc++/trunk': Var('buildtools_libcxx_url') + '@' + Var('buildtools_libcxx_revision'),
  'node-ci/buildtools/third_party/libc++abi/trunk': Var('buildtools_libcxxabi_url') + '@' + Var('buildtools_libcxxabi_revision'),
  'node-ci/buildtools/third_party/libunwind/trunk': Var('buildtools_libunwind_url') + '@' + Var('buildtools_libunwind_revision'),
  'node-ci/node': Var('node_url') + '@' + Var('node_revision'),
  'node-ci/third_party/depot_tools': Var('depot_tools_url') + '@' + Var('depot_tools_revision'),
  'node-ci/third_party/googletest/src': Var('googletest_url') + '@' + Var('googletest_revision'),
  'node-ci/third_party/icu': Var('icu_url') + '@' + Var('icu_revision'),
  'node-ci/third_party/jinja2': Var('jinja2_url') + '@' + Var('jinja2_revision'),
  'node-ci/third_party/markupsafe': Var('markupsafe_url') + '@' + Var('markupsafe_revision'),
  'node-ci/tools/clang': Var('clang_url') + '@' + Var('clang_revision'),
  'node-ci/v8': Var('v8_url') + '@' +  Var('v8_revision'),
  'node-ci/buildtools/linux64': {
    'packages': [
      {
        'package': 'gn/gn/linux-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "linux"',
  },
  'node-ci/buildtools/mac': {
    'packages': [
      {
        'package': 'gn/gn/mac-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "mac"',
  },
  'node-ci/buildtools/win': {
    'packages': [
      {
        'package': 'gn/gn/windows-amd64',
        'version': Var('gn_version'),
      }
    ],
    'dep_type': 'cipd',
    'condition': 'host_os == "win"',
  },
}

recursedeps = [
  'node-ci/buildtools',
]

hooks = [
  {
    'name': 'generate_node_filelist',
    'pattern': 'node-ci/node',
    'action': ['python', 'node-ci/tools/generate_node_files_json.py'],
  },
  {
    # Update the Windows toolchain if necessary.
    'name': 'win_toolchain',
    'pattern': '.',
    'condition': 'checkout_win',
    'action': ['python', 'node-ci/build/vs_toolchain.py', 'update'],
  },
  {
    'name': 'clang',
    'pattern': '.',
    'action': ['python', 'node-ci/tools/clang/scripts/update.py'],
  },
  {
    # Update LASTCHANGE.
    'name': 'lastchange',
    'pattern': '.',
    'action': ['python', 'node-ci/build/util/lastchange.py',
               '-o', 'node-ci/build/util/LASTCHANGE'],
  },
  {
    'name': 'sysroot_x64',
    'pattern': '.',
    'condition': 'checkout_linux and checkout_x64',
    'action': ['python',
               'node-ci/build/linux/sysroot_scripts/install-sysroot.py',
               '--arch=x64'],
  },
]
