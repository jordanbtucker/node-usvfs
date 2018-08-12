# node-usvfs
Node.js bindings for [User Space Virtual File System (USVFS)](https://github.com/modorganizer2/usvfs).

This is currently a work in progress and is probably unstable.

This only works on 64-bit Windows 10. It may work on older versions of Windows,
but I haven't tested it.

## Contributing
Cloning this repository and its dependencies will use over 1 GB of bandwidth,
about 3 GB of disk space, and a significant amount of time.

Building the dependencies will also take several minutes depending on your CPU.

Thankfully, these tasks usually need to be done only once.

### Requirements

#### Operating System
Windows 10 64-bit

#### Software
I recommend using [Scoop](https://scoop.sh/) to install the dependencies. To
install Scoop, open PowerShell, and run the following commands.

```ps
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
iwr get.scoop.sh -usebasicparsing | iex
```

To install the required software with Scoop, run the following commands.

```
scoop install git
scoop install nodejs-lts
scoop bucket add versions
scoop install python27
```

If you don't use Scoop, then you'll need to install the following dependencies
manually.

- [Git](https://git-scm.com/)
- [Node.js 8](https://nodejs.org/en/) (Other versions may work, but I haven't
  tested them.)
- [Python 2.7](https://www.python.org/) (Python 3 is not compatible.)

Regardless of whether you use Scoop, you'll need to install Visual Studio 2017
manually.

- [Visual Studio 2017](https://visualstudio.microsoft.com/vs/)
  - Workloads
    - Desktop development with C++
  - Individual components
    - Windows 10 SDK (10.0.16299.0) for Desktop C++ [x86 and x64]

To get setup quickly, download [Visual Studio 2017
Community](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=15),
then run the following command. The required components will be selected
automatically. If you already have Visual Studio 2017 installed, then this
command will update your installation with the required components.

```
vs_community.exe --add Microsoft.VisualStudio.Workload.NativeDesktop --includeRecommended --add Microsoft.VisualStudio.Component.Windows10SDK.16299.Desktop
```

Visual Studio is only required for building. I recommend using [Visual Studio
Code](https://code.visualstudio.com/) with the following extensions for code
editing.
- [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [EditorConfig](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig)
- [ESLint](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint)

#### windows-build-tools Is Not Required
When installing Node.js addons, you usually just install
[windows-build-tools](https://www.npmjs.com/package/windows-build-tools).
However, windows-build-tools installs Visual Studio 2015, and node-usvfs
requires Visual Studio 2017. If you've already installed windows-build-tools,
you don't need to uninstall it. Visual Studio 2017 and windows-build-tools can
coexist.

### Development Setup
These steps only need to be done once.

Run the following commands to clone the repository and its dependencies.

```
git clone --recurse-submodules https://github.com/jordanbtucker/node-usvfs
cd node-usvfs
npm install --ignore-scripts
npm run dev-setup
```

Grab a Snickers. This is going to take awhile.

### Building
Run the following command to build node-usvsf. This will only build the
components that have changed, which should only be the files in the `src`
directory.

```
npm run build
```

If you make a change to `binding.gyp`, you'll want a clean build. The following
command will clean the `build` directory, configure the project, and build.

```
npm run rebuild
```

### Updating Dependencies
The dependencies in the `deps` directory are git submodules pointing to specific
versions. These submodules should only be updated when
[usvfs](https://github.com/modorganizer2/usvfs)'s version is bumped. Do not
modify any files in `deps`.

### Testing
```
npm test
```
