#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xfce4-whiskermenu-plugin
Version  : 2.1.5
Release  : 15
URL      : http://mirror.netcologne.de/xfce/src/panel-plugins/xfce4-whiskermenu-plugin/2.1/xfce4-whiskermenu-plugin-2.1.5.tar.bz2
Source0  : http://mirror.netcologne.de/xfce/src/panel-plugins/xfce4-whiskermenu-plugin/2.1/xfce4-whiskermenu-plugin-2.1.5.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: xfce4-whiskermenu-plugin-bin
Requires: xfce4-whiskermenu-plugin-lib
Requires: xfce4-whiskermenu-plugin-data
Requires: xfce4-whiskermenu-plugin-locales
Requires: xfce4-whiskermenu-plugin-doc
BuildRequires : cmake
BuildRequires : pkgconfig(exo-1)
BuildRequires : pkgconfig(garcon-1)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : pkgconfig(libxfce4panel-1.0)
Patch1: 0001-Show-the-menu-label-by-default.patch

%description
About
=====
Whisker Menu is an alternate application launcher for Xfce. When you open
it you are shown a list of applications you have marked as favorites. You
can browse through all of your installed applications by clicking on the
category buttons on the side. Top level categories make browsing fast,
and simple to switch between. Additionally, Whisker Menu keeps a list of
the last ten applications that you've launched from it.

%package bin
Summary: bin components for the xfce4-whiskermenu-plugin package.
Group: Binaries
Requires: xfce4-whiskermenu-plugin-data

%description bin
bin components for the xfce4-whiskermenu-plugin package.


%package data
Summary: data components for the xfce4-whiskermenu-plugin package.
Group: Data

%description data
data components for the xfce4-whiskermenu-plugin package.


%package doc
Summary: doc components for the xfce4-whiskermenu-plugin package.
Group: Documentation

%description doc
doc components for the xfce4-whiskermenu-plugin package.


%package lib
Summary: lib components for the xfce4-whiskermenu-plugin package.
Group: Libraries
Requires: xfce4-whiskermenu-plugin-data

%description lib
lib components for the xfce4-whiskermenu-plugin package.


%package locales
Summary: locales components for the xfce4-whiskermenu-plugin package.
Group: Default

%description locales
locales components for the xfce4-whiskermenu-plugin package.


%prep
%setup -q -n xfce4-whiskermenu-plugin-2.1.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1514496875
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1514496875
rm -rf %{buildroot}
pushd clr-build
%make_install
popd
%find_lang xfce4-whiskermenu-plugin

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/xfce4-popup-whiskermenu

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/128x128/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/16x16/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/22x22/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/24x24/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/256x256/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/32x32/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/48x48/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/64x64/apps/xfce4-whiskermenu.png
/usr/share/icons/hicolor/scalable/apps/xfce4-whiskermenu.svg
/usr/share/xfce4/panel/plugins/whiskermenu.desktop

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xfce4/panel/plugins/libwhiskermenu.so

%files locales -f xfce4-whiskermenu-plugin.lang
%defattr(-,root,root,-)

