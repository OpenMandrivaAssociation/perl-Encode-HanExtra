%define upstream_name    Encode-HanExtra
%define upstream_version 0.23

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.230.0-4
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-3mdv2011.0
+ Revision: 555798
- rebuild for perl 5.12

* Fri Mar 12 2010 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-2mdv2010.1
+ Revision: 518455
- ship debug files in -debug

* Mon Jul 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.230.0-1mdv2010.0
+ Revision: 392895
- adding missing buildrequires:
- import perl-Encode-HanExtra


* Mon Jul 06 2009 cpan2dist 0.23-1mdv
- initial mdv release, generated with cpan2dist
