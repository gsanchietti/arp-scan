Name:           arp-scan
Version:        1.9.2
Release:        1%{?dist}
Summary:        Scanning and fingerprinting tool

Group:          Applications/Internet
# Includes getopt, which is LGPLv2+, but the whole is GPLv2+.
License:        GPLv2+
URL:            http://www.nta-monitor.com/tools/arp-scan/
Source0:        http://www.nta-monitor.com/tools/arp-scan/download/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libpcap-devel
BuildRequires:  perl-generators
Requires:       perl(LWP::Simple)


%description
arp-scan is a command-line tool that uses the ARP protocol to discover and
fingerprint IP hosts on the local network.

%prep
%setup -q

%build
#install to sbindir
%configure --bindir=%{_sbindir}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

#fix permissions for -debuginfo package
chmod 0644 $RPM_BUILD_DIR/%{name}-%{version}/mt19937ar.c

#fix permissions for files in sbindir
chmod 0755 $RPM_BUILD_ROOT%{_sbindir}/*

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README TODO 
%{_sbindir}/*
%{_datadir}/arp-scan
%{_mandir}/man?/*


%changelog
* Wed Jul 27 2016 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.9.2-1
- upgrade to git version, fix #1359953

* Fri Jul 15 2016 xmrbrz <brunorobertozanuzzo@gmail.com> - 1.9-1
- rebuilt for new version 1.9

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.8.4-2
- Perl 5.18 rebuild

* Mon May 13 2013 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.8.4-1
- new version 1.8.4

* Wed May 08 2013 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.8-1
- new version 1.8

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Nov 11 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.7-2
- no luck with cvs commit, reimporting new SRPM version via cvs-import.sh

* Tue Nov 11 2008 Itamar Reis Peixoto <itamar@ispbrasil.com.br> 1.7-1
- upgrade to new version

* Mon Jul 14 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.6-3
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.6-2
- Autorebuild for GCC 4.3

* Sun May 06 2007 Sindre Pedersen Bjørdal <foolish[AT]guezz.net> - 1.6-1
- Initial build
