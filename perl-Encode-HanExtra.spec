%define	upstream_name	Encode-HanExtra

Name:		perl-Encode-HanExtra
Version:	0.23
Release:	1
Summary:	Extra sets of Chinese encodings
License:	MIT
Group:		Development/Perl
URL:		https://metacpan.org/dist/Encode-HanExtra
Source0:	https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Encode-HanExtra-0.23.tar.gz
Source1:	enc2xs
Source2:	encode.h

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Encode)
BuildRequires:	perl-Encode
BuildRequires:	gcc

%description
Extra sets of Chinese encodings.

%prep
%autosetup -n %{upstream_name}-%{version}

%build
install -m755 %{SOURCE1} enc2xs
mkdir -p Encode
install -m644 %{SOURCE2} Encode/encode.h
export PATH="$PWD:$PATH"
export PERL5LIB="$PWD${PERL5LIB:+:$PERL5LIB}"
perl Makefile.PL INSTALLDIRS=vendor
%make_build OPTIMIZE="%{optflags}"

%install
%make_install
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
find %{buildroot} -type d -empty -delete

%files
%{perl_vendorarch}/*
