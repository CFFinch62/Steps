"""Setup script for tree-sitter-steps Python bindings."""

from setuptools import setup, Extension
from pathlib import Path

# Read the README for long description
readme_path = Path(__file__).parent / "README.md"
long_description = ""
if readme_path.exists():
    long_description = readme_path.read_text(encoding="utf-8")

# Tree-sitter Steps language extension
steps_language = Extension(
    "tree_sitter_steps.binding",
    sources=[
        "src/parser.c",
        "bindings/python/binding.c",
    ],
    include_dirs=["src"],
    extra_compile_args=["-std=c11"] if not Path("/").drive else [],
)

setup(
    name="tree-sitter-steps",
    version="1.0.0",
    description="Tree-sitter grammar for the Steps programming language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Steps Language Team",
    license="MIT",
    packages=["tree_sitter_steps"],
    package_dir={"tree_sitter_steps": "bindings/python/tree_sitter_steps"},
    ext_modules=[steps_language],
    python_requires=">=3.8",
    install_requires=[
        "tree-sitter>=0.20.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Compilers",
        "Topic :: Text Processing :: Linguistic",
    ],
    keywords="tree-sitter parser steps programming-language",
    project_urls={
        "Source": "https://github.com/yourusername/tree-sitter-steps",
    },
)

