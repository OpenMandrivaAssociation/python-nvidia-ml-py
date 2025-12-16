Name:		python-nvidia-ml-py
Version:	13.590.44
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/n/nvidia-ml-py/nvidia_ml_py-%{version}.tar.gz
Summary:	Python Bindings for the NVIDIA Management Library
URL:		https://pypi.org/project/nvidia-ml-py/
License:	BSD
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Python Bindings for the NVIDIA Management Library

%files
%{py_sitedir}/pynvml.py
%{py_sitedir}/example.py
%{py_sitedir}/nvidia_ml_py-*.*-info
