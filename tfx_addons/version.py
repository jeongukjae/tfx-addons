# Copyright 2022 The TensorFlow Authors. All Rights Reserved.

# TODO: This license is not consistent with license used in the project.
#       Delete the inconsistent license and above line and rerun pre-commit to insert a good license.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#   http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Define TFX Addons version information."""

# Required TFX version [min, max), keep depconstraint in ci.yml in sync.
INCLUSIVE_MIN_TFX_VERSION = "1.4.0"
EXCLUSIVE_MAX_TFX_VERSION = "1.8.0"

# We follow Semantic Versioning (https://semver.org/).
_MAJOR_VERSION = "0"
_MINOR_VERSION = "1"
_PATCH_VERSION = "0"

# When building releases, we can update this value on the release branch to
# reflect the current release candidate ('rc0', 'rc1') or, finally, the official
# stable release (indicated by `_VERSION_SUFFIX = ''`). Outside the context of a
# release branch, the current version is by default assumed to be a
# 'development' version, labeled 'dev'.
_VERSION_SUFFIX = "rc0"

# Example, '0.1.0-dev'
__version__ = ".".join([_MAJOR_VERSION, _MINOR_VERSION, _PATCH_VERSION])
if _VERSION_SUFFIX:
  __version__ = "{}-{}".format(__version__, _VERSION_SUFFIX)
