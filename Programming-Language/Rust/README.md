
# Install

+ win：使用`scoop`（虽然官方推荐`rustup`），正常的search和install后会出现

	```bash
	Installing 'rust' (1.74.0) [64bit] from main bucket
	rust-1.74.0-x86_64-pc-windows-msvc.msi (218.0 MB) [===========================================================] 100%
	Checking hash of rust-1.74.0-x86_64-pc-windows-msvc.msi ... ok.
	Extracting rust-1.74.0-x86_64-pc-windows-msvc.msi ... done.
	Linking D:\Scoop\apps\rust\current => D:\Scoop\apps\rust\1.74.0
	Creating shim for 'rustc'.
	Creating shim for 'rustdoc'.
	Creating shim for 'cargo'.
	'rust' (1.74.0) was installed successfully!
	Notes
	-----
	Use the rustup package instead for easier management of multiple toolchains, including beta/nightly releases.
	According to https://doc.rust-lang.org/book/ch01-01-installation.html#installing-rustup-on-windows
	Microsoft C++ Build Tools is needed and can be downloaded here:
	https://visualstudio.microsoft.com/visual-cpp-build-tools/
	When installing build tools, these two components should be selected:
	- MSVC - VS C++ x64/x86 build tools
	- Windows SDK
	```

	按照上面的要求下载对应的组件即可

	+ 你可能没有被Visual Studio恶心过，这里聊几点
		+ 官网链接的可执行文件是“Visual Studio Installer”的Install，它的路径似乎不能修改，但是"Installer"下载的东西的路径是可以修改的，记得修改。
		+ 你可能没有立刻找到上面提到的两个组件，别着急，慢慢找，点击点击试试，记得别下载多余的组件。

