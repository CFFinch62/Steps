#!/usr/bin/env python3
"""Test minimal query to isolate the issue."""

from tree_sitter import Language, Query
import tree_sitter_steps

lang = Language(tree_sitter_steps.language())

# Test queries one by one
queries = [
    ('Comments', '(comment) @comment'),
    ('Building', '"building:" @keyword'),
    ('Do keyword', '"do:" @keyword'),
    ('Exit statement', '(exit_statement) @keyword'),
    ('Type node', '(type) @type'),
    ('Building def', '(building_def) @structure'),
    ('Building def with identifier', '(building_def (identifier) @namespace)'),
]

for name, query_text in queries:
    try:
        query = Query(lang, query_text)
        print(f"✓ {name}: OK")
    except Exception as e:
        print(f"✗ {name}: {e}")

