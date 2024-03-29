%define _disable_rebuild_configure 1

Summary:        Ncurses interface for QEMU
Name:           nemu
Version:        3.0.0
Release:        1
License:        GPLv2+
Group:          Monitoring
Url:            https://lib.void.so/nemu/ 
Source0:        https://github.com/nemuTUI/nemu/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
#Source0:	https://bitbucket.org/PascalRD/nemu/get/v%{version}.tar.gz
BuildRequires:  pkgconfig(spice-protocol)
BuildRequires:	graphviz-devel
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(json-c)
Requires:	qemu


%description
ncurses interface for QEMU

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DNM_WITH_SPICE=ON -DNM_WITH_OVF_SUPPORT=ON -DNM_WITH_NETWORK_MAP=ON
%make_build

%install
%make_install -C build

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/ntty
%{_datadir}/%{name}/scripts/42-net-macvtap-perm.rules
%{_datadir}/%{name}/scripts/setup_nemu_nonroot.sh
%{_datadir}/%{name}/scripts/upgrade_db.sh
%{_datadir}/%{name}/templates/config/nemu.cfg.sample
%{_datadir}/%{name}/scripts/nemu.bash
%{_datadir}/bash-completion/completions/nemu
%{_mandir}/man1/nemu.1.zst
