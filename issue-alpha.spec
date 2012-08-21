
%bcond_with	snap	# include shapshot information in version,
			# should be used only in official Th spanhots

%define snapshot	2012

# CPE_NAME = cpe:/ {part} : {vendor} : {product} : {version} : {update} : {edition} : {language}
# http://cpe.mitre.org/specification/
# http://csrc.nist.gov/publications/nistir/ir7695/NISTIR-7695-CPE-Naming.pdf

%if %{with snap}
%define	distname	Th/%{snapshot}
%define cpename		cpe:/o:pld-linux:pld:%{distversion}:%{snapshot}
%else
%define	distname	Th
%define cpename		cpe:/o:pld-linux:pld:%{distversion}
%endif
%define	distversion	3.0
%define	distrelease	"%{distversion} PLD Linux (%{distname})"

Summary:	PLD Linux release file with virtual keyboard
Summary(pl.UTF-8):	Wersja Linuksa PLD z wirtualną klawiaturą
Name:		issue-alpha
Version:	%{distversion}
Release:	1%{?with_snap:.%{snapshot}}
License:	GPL
Group:		Base
Provides:	issue
Provides:	issue-package
Obsoletes:	issue-package
Conflicts:	issue-fancy < 3.0
Conflicts:	issue-logo < 3.0
Conflicts:	issue-nice < 3.0
Conflicts:	issue-pure < 3.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD Linux release file with virtual keyboard. Can be used to some
hacks with gpm on systems w/o available keyboard or as paranoic
security login solution (anti keyloggers).

%description -l pl.UTF-8
Wersja Linuksa PLD z wirtualną klawiaturą. Może być użyta do manewrów
za pomocą gpma w systemach bez sprawnej klawiatury, bądź jako poprawa
bezpieczeństwa logowania dla paranoików (przeciwdziała keyloggerom).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

cat > $RPM_BUILD_ROOT%{_sysconfdir}/issue.net <<EOF
.-------------< PLD Linux %{distversion} (%{distname}) >--------------.
|                                                 |
|  ~  !  "  #  $  %  ^  &  *  (  )  _  +          |
| ' \`  1  2  3  4  5  6  7  8  9  0  -  =         |
|                                                :'
|                                {  }            ;
|  Qq Ww Ee Rr Tt Yy Uu Ii Oo Pp  [  ]          ;
|                               :  @  ~       .;
|    Aa Ss Dd Ff Gg Hh Jj Kk Ll  ;  '  #     :;
:   |                       <  >  ?        .;'
\`:   \\\\ Zz Xx Cc Vv Bb Nn Mm  ,  .  /   ,.;'"
  \`..                           ,..;:'"
     \`-------------------------'

EOF

cat $RPM_BUILD_ROOT%{_sysconfdir}/issue.net > $RPM_BUILD_ROOT%{_sysconfdir}/issue
echo -ne "\l " >> $RPM_BUILD_ROOT%{_sysconfdir}/issue

echo %{distrelease} > $RPM_BUILD_ROOT%{_sysconfdir}/pld-release

# CPE_NAME = cpe:/ {part} : {vendor} : {product} : {version} : {update} : {edition} : {language}
# http://cpe.mitre.org/specification/
cat >$RPM_BUILD_ROOT%{_sysconfdir}/os-release <<EOF
NAME="PLD Linux"
VERSION="%{distversion} (%{distname})"
ID="pld"
VERSION_ID="%{distversion}"
PRETTY_NAME="PLD Linux %{distversion} (%{distname})"
ANSI_COLOR="0;32"
CPE_NAME="%{cpename}"
HOME_URL="http://www.pld-linux.org/"
BUG_REPORT_URL="https://bugs.launchpad.net/pld-linux/"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/os-release
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
