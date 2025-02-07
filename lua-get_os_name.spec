%define luarocks_pkg_name get_os_name
%define luarocks_pkg_version 0.0.1-1
%define luarocks_pkg_prefix get_os_name-0.0.1-1
%define luarocks_pkg_major 0.0.1
%define luarocks_pkg_minor 1
%global __luarocks_requires %{_bindir}/true
%global __luarocks_provides %{_bindir}/true

Name: lua-get_os_name
BuildRequires: lua-rpm-macros

%if %{defined luarocks_requires}
%luarocks_requires
%else
BuildRequires: lua54-luarocks lua53-luarocks lua51-luarocks
BuildRequires: lua54-devel lua53-devel lua51-devel
BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: make
%endif
Version: %{luarocks_pkg_major}
Release: %{luarocks_pkg_minor}
Summary: Get OS name and architecture
Url: https://github.com/huakim/lua_get_os_name
License: LGPL
Provides: %{luadist %{luarocks_pkg_name} = %{luarocks_pkg_version}}
Requires: %{luadist lua >= 5.1}

Source0: get_os_name-0.0.1-1.tar.gz
Source1: get_os_name-0.0.1-1.rockspec
%{?luarocks_subpackages:%luarocks_subpackages -f}

%description
  

%prep
%autosetup -p1 -n %luarocks_pkg_prefix
%luarocks_prep

%generate_buildrequires

%build
%{?luarocks_subpackages_build}
%{!?luarocks_subpackages_build:%luarocks_build}

%install
%{?luarocks_subpackages_install}
%{!?luarocks_subpackages_install:%luarocks_install %{luarocks_pkg_prefix}.*.rock}
%{?lua_generate_file_list}
%check
%if %{with check}
%{?luarocks_check}
%endif

%files %{?lua_files}%{!?lua_files:-f lua_files.list}
