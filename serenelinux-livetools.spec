Summary: serenelinux livetools
Name: serenelinux-livetools
Version: 1.0.3
Release: 2%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

Source0: https://github.com/FascodeNet/fascode-live-tools/archive/master.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux livetools
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n fascode-live-tools-master

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
cp -arf ./fascode-gtk-bookmarks/fascode-gtk-bookmarks $RPM_BUILD_ROOT/usr/bin/
chmod +x $RPM_BUILD_ROOT/usr/bin/fascode-gtk-bookmarks
ln -s /usr/bin/fascode-gtk-bookmarks $RPM_BUILD_ROOT/usr/bin/serenelinux-gtk-bookmarks


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
/usr/bin/serenelinux-gtk-bookmarks
%changelog
