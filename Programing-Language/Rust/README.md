# Install

## Windows
>我这里使用Scoop

1. `scoop install rust`
	提示：
	```
	Notes
	-----
	This package defaults to using the MSVC toolchain in new installs; use "rustup set
	default-host" to configure it
	(existing installs may be using the GNU toolchain by default)
	According to
	https://doc.rust-lang.org/book/ch01-01-installation.html#installing-rustup-on-windows
	Microsoft C++ Build Tools is needed and can be downloaded here:
	https://visualstudio.microsoft.com/visual-cpp-build-tools/
	When installing build tools, these two components should be selected:
	- MSVC - VS C++ x64/x86 build tools
	- Windows SDK
	```
	按照提示下载即可
	+ 安装了`rustc`和`cargo`

2. `scoop install rustup`