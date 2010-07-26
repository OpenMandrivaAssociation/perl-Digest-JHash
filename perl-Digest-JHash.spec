%define upstream_name    Digest-JHash
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Perl extension for 32 bit Jenkins Hashing Algorithm
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
# We need to convert .gz into .lzma and make world-writable files only
# user-writable.
Source0:    http://www.cpan.org/modules/by-module/Digest/%{upstream_name}-%{upstream_version}.tar.lzma


BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


