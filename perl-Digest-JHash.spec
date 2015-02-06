%define upstream_name    Digest-JHash
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Perl extension for 32 bit Jenkins Hashing Algorithm
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Digest/Digest-JHash-%{upstream_version}.tar.gz

BuildRequires: perl-devel

%description
The 'Digest::JHash' module allows you to use the fast JHash hashing
algorithm developed by Bob Jenkins from within Perl programs. The algorithm
takes as input a message of arbitrary length and produces as output a
32-bit "message digest" of the input in the form of an unsigned long
integer.

Call it a low calorie version of MD5 if you like.

See http://burtleburtle.net/bob/hash/doobs.html for more information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%clean

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.70.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2
+ Revision: 681420
- mass rebuild

* Mon Sep 06 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 576295
- update to 0.07

* Thu Jul 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 562995
- update to 0.06

* Mon Jul 26 2010 Shlomi Fish <shlomif@mandriva.org> 0.50.0-1mdv2011.0
+ Revision: 560763
- import perl-Digest-JHash


* Thu Jul 22 2010 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist

