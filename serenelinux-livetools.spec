Summary: serenelinux livetools
Name: serenelinux-livetools
Version: 1.0.3
Release: 1%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux livetools
%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/bin/
curl "https://raw.githubusercontent.com/FascodeNet/fascode-live-tools/844da4ef01c9c05b4428630a39331b05923c2bcb/fascode-gtk-bookmarks/fascode-gtk-bookmarks" > %{buildroot}/usr/bin/fascode-gtk-bookmarks
ln -s /usr/bin/fascode-gtk-bookmarks %{buildroot}/usr/bin/serenelinux-gtk-bookmarks

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
/usr/bin/fascode-gtk-bookmarks
/usr/bin/serenelinux-gtk-bookmarks
%changelog
