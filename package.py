name = 'zlib'

version = '1.3.2.hh.1.0.0'

authors = [
    'Zlib',
]

description = '''Zlib'''

with scope('config') as c:
    import os
    c.release_packages_path = os.environ['HH_REZ_REPO_RELEASE_EXT']
    c.plugins.release_hook.hh_emailer.recipients = []

requires = [
]

private_build_requires = [
]

variants = [
]

def commands():
    env.REZ_ZLIB_ROOT = '{root}'
    env.ZLIB_ROOT = '{root}'
    env.PKG_CONFIG_PATH.append("{root}/lib/cmake/zlib")
    env.PATH.append("{root}/bin")


build_system = "cmake"
uuid = 'repository.zlib'
