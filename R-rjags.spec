#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rjags
Version  : 4.10
Release  : 24
URL      : https://cran.r-project.org/src/contrib/rjags_4-10.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rjags_4-10.tar.gz
Summary  : Bayesian Graphical Models using MCMC
Group    : Development/Tools
License  : GPL-2.0
Requires: R-rjags-lib = %{version}-%{release}
Requires: R-coda
BuildRequires : JAGS-dev
BuildRequires : R-coda
BuildRequires : buildreq-R

%description
No detailed description available

%package lib
Summary: lib components for the R-rjags package.
Group: Libraries

%description lib
lib components for the R-rjags package.


%prep
%setup -q -c -n rjags
cd %{_builddir}/rjags

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589523312

%install
export SOURCE_DATE_EPOCH=1589523312
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rjags
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rjags
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rjags
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rjags || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rjags/DESCRIPTION
/usr/lib64/R/library/rjags/INDEX
/usr/lib64/R/library/rjags/Meta/Rd.rds
/usr/lib64/R/library/rjags/Meta/data.rds
/usr/lib64/R/library/rjags/Meta/features.rds
/usr/lib64/R/library/rjags/Meta/hsearch.rds
/usr/lib64/R/library/rjags/Meta/links.rds
/usr/lib64/R/library/rjags/Meta/nsInfo.rds
/usr/lib64/R/library/rjags/Meta/package.rds
/usr/lib64/R/library/rjags/NAMESPACE
/usr/lib64/R/library/rjags/R/rjags
/usr/lib64/R/library/rjags/R/rjags.rdb
/usr/lib64/R/library/rjags/R/rjags.rdx
/usr/lib64/R/library/rjags/data/LINE.RData
/usr/lib64/R/library/rjags/help/AnIndex
/usr/lib64/R/library/rjags/help/aliases.rds
/usr/lib64/R/library/rjags/help/paths.rds
/usr/lib64/R/library/rjags/help/rjags.rdb
/usr/lib64/R/library/rjags/help/rjags.rdx
/usr/lib64/R/library/rjags/html/00Index.html
/usr/lib64/R/library/rjags/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/rjags/libs/rjags.so
