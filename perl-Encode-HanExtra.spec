%define upstream_name    Encode-HanExtra
%define upstream_version 0.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Extra sets of Chinese encodings
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Encode/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Encode)
BuildRequires: perl-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl 5.7.3 and later ships with an adequate set of Chinese encodings,
including the commonly used 'CP950', 'CP936' (also known as 'GBK'), 'Big5'
(alias for 'Big5-Eten'), 'Big5-HKSCS', 'EUC-CN', 'HZ', and 'ISO-IR-165'.

However, the numbers of Chinese encodings are staggering, and a complete
coverage will easily increase the size of perl distribution by several
megabytes; hence, this CPAN module tries to provide the rest of them.

If you are using Perl 5.8 or later, the Encode::CN manpage and the
Encode::TW manpage will automatically load the extra encodings for you, so
there's no need to explicitly write 'use Encode::HanExtra' if you are using
one of them already.

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
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
