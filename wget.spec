Name: wget
Version: 1.8.2
Release: alt4

Summary: An utility for retrieving files using the HTTP, HTTPS or FTP protocols
License: GPL
Group: Networking/WWW
Url: http://www.gnu.org/directory/GNU/%name.html

Source: ftp://ftp.gnu.org/gnu/%name/%name-%version.tar.bz2

Patch1: %name-1.8.2-alt-texinfo.patch
Patch2: %name-1.6-mdk-passive_ftp.patch
Patch3: %name-1.7-alt-locale.patch
Patch4: %name-1.8.1-alt-quiet.patch
Patch5: %name-1.8.1-mdk-netrc.patch
Patch6: %name-1.8.2-rh-ht.patch
Patch7: %name-1.8.2-rh-alt-filename.patch
Patch8: %name-1.8.2-rh-segv.patch

Requires(post,preun): %__install_info

# Automatically added by buildreq on Wed Dec 11 2002
BuildRequires: glibc-devel-static libssl-devel

%description
GNU Wget is a file retrieval utility which can use either the HTTP,
HTTPS or FTP protocols.  Wget features include the ability to work
in the background while you're logged out, recursive retrieval of
directories, file name wildcard matching, remote file timestamp
storage and comparison, use of Rest with FTP servers and Range with
HTTP servers to retrieve files over slow or unstable connections,
support for Proxy servers, and configurability.

Install wget if you need to retrieve large numbers of files with HTTP,
HTTPS or FTP, or if you need a utility for mirroring web sites or FTP
directories.

%prep
%setup -q

# Fix docs and samples.
%__rm -f doc/*.info*
find doc -type f -print0 |
	xargs -r0 %__grep -FZl /usr/local/ -- |
	xargs -r0 %__subst 's,/usr/local/,/,g' --

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p0
%patch7 -p1
%patch8 -p1

%build
%configure --with-ssl
%make_build

%install
%makeinstall

%find_lang %name

%post
%install_info %name.info

%preun
%uninstall_info %name.info

%files -f %name.lang
%config(noreplace) %_sysconfdir/%{name}rc
%_bindir/*
%_mandir/man?/*
%_infodir/*.info*
%doc AUTHORS MACHINES MAILING-LIST NEWS README* TODO

%changelog
* Wed Aug 06 2003 Alexey Voinov <voins@altlinux.ru> 1.8.2-alt4
- updated rh-filename patch.
- fixup wrong fix for directory traversal bug
- fixed buffer overflow (rh-segv patch)

* Wed Dec 11 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.2-alt3
- Merged RH patches:
  * Sat Oct 05 2002 Karsten Hopp <karsten@redhat.de> 1.8.2-5
  - fix directory traversal bug
  * Thu Jul 25 2002 Trond Eivind Glomsrød <teg@redhat.com> 1.8.2-3
  - Don't segfault when downloading URLs A-B-A (A-A-B worked) #49859

* Fri Nov 15 2002 Stanislav Ievlev <inger@altlinux.ru> 1.8.2-alt2
- rebuild

* Thu Jun 06 2002 Dmitry V. Levin <ldv@altlinux.org> 1.8.2-alt1
- 1.8.2
- Fixed .netrc quotation parsing (mdk).

* Tue Feb 05 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.8.1-alt1
- 1.8.1

* Tue Dec 18 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.8-alt1
- 1.8

* Tue Nov 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.7.1-alt1
- 1.7.1

* Mon Oct 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.7-alt2
- Shutup output to screen when using quiet with batch mode (rh).

* Fri Jun 15 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.7-alt1
- 1.7
- Merged some MDK and RH paches.
- Resurrected manpage.

* Fri Apr 06 2001 Sergie Pugachev <fd_rag@altlinux.ru> 1.6-alt2
- New version 1.6
- Fixed texinfo.patch
- Fixed encdec.patch
- Fixed i18n

* Sat Dec 09 2000 Dmitry V. Levin <ldv@fandra.org> 1.5.3gold-ipl2
- Fixed texinfo documentation.
- Fix bug: the characters ";/?=&+" must retain their encoded/decodedstatus.
  (from Anon Sricharoenchai <ans@beethoven.cpe.ku.ac.th>)

* Fri Jun 30 2000 Dmitry V. Levin <ldv@fandra.org> 1.5.3gold-ipl1
- RE and Fandra adaptions.

* Mon Jun 26 2000 Soenke J. Peters <soenke+rpm@simprovement.com>
- included some stuff from CVS tree
- HTTPS support

* Thu Aug 26 1999 Jeff Johnson <jbj@redhat.com>
- don't permit chmod 777 on symlinks (#4725).

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Fri Dec 18 1998 Bill Nottingham <notting@redhat.com>
- build for 6.0 tree
- add Provides

* Sat Oct 10 1998 Cristian Gafton <gafton@redhat.com>
- strip binaries
- version 1.5.3

* Sat Jun 27 1998 Jeff Johnson <jbj@redhat.com>
- updated to 1.5.2

* Thu Apr 30 1998 Cristian Gafton <gafton@redhat.com>
- modified group to Applications/Networking

* Wed Apr 22 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to 1.5.0
- they removed the man page from the distribution (Duh!) and I added it back
  from 1.4.5. Hey, removing the man page is DUMB!

* Fri Nov 14 1997 Cristian Gafton <gafton@redhat.com>
- first build against glibc

