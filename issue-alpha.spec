
%define	distname	Th
%define	distversion	2.99
%define	distrelease	"%{distversion} PLD Linux (%{distname})"

Summary:	PLD Linux release file with virtual keyboard
Summary(pl.UTF-8):	Wersja Linuksa PLD z wirtualną klawiaturą
Name:		issue-alpha
Version:	%{distversion}
Release:	4
License:	GPL
Group:		Base
Provides:	issue
Provides:	issue-package
Obsoletes:	issue-package
Conflicts:	issue-fancy < 2.99-2
Conflicts:	issue-logo < 2.99-2
Conflicts:	issue-pure < 2.99-5
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
CPE_NAME="cpe:/o:pld-linux:pld:%{distversion}"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/os-release
%{_sysconfdir}/pld-release
%config(noreplace) %{_sysconfdir}/issue*
