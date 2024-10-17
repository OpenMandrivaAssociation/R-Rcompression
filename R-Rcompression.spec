%global packname  Rcompression
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.93_2
Release:          3
Summary:          In-memory decompression for GNU zip and bzip2 formats
Group:            Sciences/Mathematics
License:          zlib. See LICENSE.
URL:              https://www.omegahat.org/Rcompression/
Source0:          http://www.omegahat.org/Rcompression/Rcompression_0.93-2.tar.gz
Requires:         R-methods 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods

%description
The package is a basic interface to some of the compression facilities in
the zlib and bzip2 libraries for uncompressing (and compressing) data in
memory that is not in a file. It handles bz2, gzip and regular compress
(.Z) content.  It can work on files or with data in memory, e.g.
downloaded directly into memory via an HTTP request.  It is used when we
don't want to write data to a file and then read it back into R. This is
common when performing HTTP requests via the RCurl package and dependent
packages such as SSOAP.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/sampleData


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.93_2-1
+ Revision: 775542
- Import R-Rcompression
- Import R-Rcompression

