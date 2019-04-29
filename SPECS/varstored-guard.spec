Name: varstored-guard
Summary: Deprivileged XAPI socket Daemon for EFI variable storage
Version: 0.3.0
Release: 1

License: LGPL
URL:            https://github.com/xapi-project/varstored-guard

Source0: https://code.citrite.net/rest/archive/latest/projects/XSU/repos/varstored-guard/archive?at=v0.3.0&format=tar.gz&prefix=varstored-guard-0.3.0#/varstored-guard-0.3.0.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/varstored-guard/archive?at=v0.3.0&format=tar.gz&prefix=varstored-guard-0.3.0#/varstored-guard-0.3.0.tar.gz) = f87168cfc09401bf5f09259c39ce3be352832a5c

BuildRequires:  ocaml-xcp-idl-devel ocaml-xen-api-client-devel openssl-devel xs-opam-repo

%{?systemd_requires}

%description
A daemon for implementing a deprivileged XAPI socket for varstored.
It is responsible for giving access only to a specific VM to varstored.

%prep
%autosetup -p1

%build
make

%install
opam-installer -i --prefix %{buildroot}/usr --mandir %{buildroot}%{_mandir}
install -D -m 644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service

%check
make check

%files
%license LICENSE
%{_sbindir}/*
%{_unitdir}/%{name}.service
%exclude /usr/lib/%{name}/META
%exclude /usr/lib/%{name}/opam
%exclude /usr/doc/%{name}/LICENSE

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%changelog
* Tue Jan 22 2019 Christian Lindig <christian.lindig@citrix.com> - 0.3.0-1
- CA-308072: fix varstored-guard with toolstack restart
- CA-308072: wait for unix socket to be connectable
- CA-308072: do not swallow errors from creating the http server

* Tue Dec 18 2018 Edwin Török <edvin.torok@citrix.com> - 0.2.0-1
- CA-302981: Timeout on XAPI calls
- CP-30032: sandboxing support for varstore-rm
- Merge from master: rename xcp to xapi-idl

* Thu Nov 22 2018 Edwin Török <edvin.torok@citrix.com> - 0.1.0-1
- Initial packaging
