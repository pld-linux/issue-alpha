%define		distversion	%(. /etc/os-release 2>/dev/null ; echo $VERSION)

Summary:	PLD Linux release file with virtual keyboard
Summary(pl.UTF-8):	Wersja Linuksa PLD z wirtualną klawiaturą
Name:		issue-alpha
Version:	3.0
Release:	24
License:	GPL
Group:		Base
BuildRequires:	pld-release >= 3.0
%requires_eq	pld-release
Provides:	issue = %{version}-%{release}
Conflicts:	issue-fancy < 3.0-1
Conflicts:	issue-logo < 3.0-1
Conflicts:	issue-nice < 3.0-1
Conflicts:	issue-pure < 3.0-1
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
.-------------< PLD Linux %{distversion} >--------------.
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %{_sysconfdir}/issue*
