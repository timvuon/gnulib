# options to filter out, and why
--all-warnings				alias for -Wall
--extra-warnings			alias for -Wextra
-Waggregate-return			obsolescent
-Waliasing				fortran
-Walign-commons				fortran
-Wampersand				fortran
-Warray-temporaries			fortran
-Wassign-intercept			objc/objc++
-Wc++-compat				FIXME maybe? borderline.  some will want this
-Wc++0x-compat				c++
-Wc++11-compat				c++
-Wc-binding-type			fortran
-Wc-binding-type                        fortran
-Wcast-qual				FIXME maybe? too much noise; encourages bad changes
-Wcharacter-truncation			fortran
-Wcompare-reals                         fortran
-Wconversion				FIXME maybe? too much noise; encourages bad changes
-Wconversion-extra			fortran
-Wconversion-null			c++ and objc++
-Wctor-dtor-privacy			c++
-Wdeclaration-after-statement		FIXME: do not want.  others may
-Wdeclaration-after-statement           obsolescent
-Wdelete-non-virtual-dtor		c++
-Weffc++				c++
-Werror-implicit-function-declaration	deprecated
-Wfloat-equal				FIXME maybe? borderline.  some will want this
-Wformat				covered by -Wformat=2
-Wformat=				gcc --help=warnings artifact
-Wfunction-elimination			fortran
-Wimplicit-interface			fortran
-Wimplicit-procedure			fortran
-Wintrinsic-shadow			fortran
-Wintrinsics-std			fortran
-Winvalid-offsetof			c++ and objc++
-Wlarger-than-				gcc --help=warnings artifact
-Wlarger-than=<number>			FIXME: choose something sane?
-Wline-truncation			fortran
-Wliteral-suffix			c++ and objc++
-Wliteral-suffix                        c++ and objc++
-Wlong-long				obsolescent
-Wnoexcept				c++
-Wnon-template-friend			c++
-Wnon-virtual-dtor			c++
-Wnormalized=<id|nfc|nfkc>		FIXME: choose something sane?
-Wold-style-cast			c++ and objc++
-Woverloaded-virtual			c++
-Wpadded				FIXME: dunno
-Wpadded                                FIXME maybe?  warns about "stabil" member in /usr/include/bits/timex.h
-Wpedantic				FIXME: too strict?
-Wpmf-conversions			c++ and objc++
-Wproperty-assign-default		objc++
-Wprotocol				objc++
-Wreal-q-constant			fortran
-Wrealloc-lhs				fortran
-Wrealloc-lhs                           fortran
-Wrealloc-lhs-all			fortran
-Wrealloc-lhs-all                       fortran
-Wredundant-decls			FIXME maybe? many _gl_cxxalias_dummy FPs
-Wreorder				c++ and objc++
-Wselector				objc and objc++
-Wsign-compare				FIXME maybe? borderline.  some will want this
-Wsign-conversion			FIXME maybe? borderline.  some will want this
-Wsign-promo				c++ and objc++
-Wstack-usage=				FIXME: choose something sane?
-Wstrict-aliasing=			FIXME: choose something sane?
-Wstrict-null-sentinel			c++ and objc++
-Wstrict-overflow=			FIXME: choose something sane?
-Wstrict-selector-match			objc and objc++
-Wsurprising				fortran
-Wswitch-enum				FIXME maybe? borderline.  some will want this
-Wsynth					deprecated
-Wtabs					fortran
-Wtarget-lifetime                       fortran
-Wtraditional				obsolescent
-Wtraditional-conversion		obsolescent
-Wundeclared-selector			objc and objc++
-Wundef					FIXME maybe? too many false positives
-Wunderflow				fortran
-Wunsuffixed-float-constants            triggers warning in gnulib's timespec.h
-Wunused-dummy-argument			fortran
-Wuseless-cast				c++ and objc++
-Wuseless-cast                          c++ and objc++
-Wzero-as-null-pointer-constant		c++ and objc++
-frequire-return-statement		go