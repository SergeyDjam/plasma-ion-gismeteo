%global ion_name gismeteo

Name:           kde-plasma-ion-gismeteo
Version:        0.1
Release:        1%{?dist}
Summary:        KDE Plasma Ion data provider for Gismeteo

Group:          User Interface/Desktops
License:        GPLv2+
URL:            http://kde-apps.org/content/show.php?content=
Source0:        plasma-ion-gismeteo-%{version}.tar.bz2

BuildRequires:  cmake qt-devel kdelibs-devel kdebase-workspace-devel qt-qlibxmlnodemodel-devel

%description
KDE Plasma Ion data provider for retrieving weather information from Gismeteo.


%prep
%setup -q -n plasma-ion-gismeteo


%build
%{cmake_kde4} -DCMAKE_BUILD_TYPE=Debug
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc CHANGELOG COPYING README
%{_libdir}/kde4/ion_%{ion_name}.so
%{_datadir}/kde4/apps/plasma-ion-%{ion_name}/%{ion_name}.xq
%{_datadir}/kde4/apps/plasma-ion-%{ion_name}/%{ion_name}-search.xq
%{_datadir}/kde4/services/ion-%{ion_name}.desktop


%changelog
* Thu Jan 11 2012 Alexey Torkhov <atorkhov@gmail.com> - 0.1-1
- Initial package.
