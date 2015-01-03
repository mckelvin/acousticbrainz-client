# Copyright 2014 Music Technology Group - Universitat Pompeu Fabra
# acousticbrainz-client is available under the terms of the GNU
# General Public License, version 3 or higher. See COPYING for more details.

has_acoustid = False
try:
    import acoustid
    has_acoustid = True
except ImportError:
    pass


# key used in Picard: http://dou.bz/2J6P6q
ACOUSTID_API_KEY = 'tPrbdkhM'


def acoustid_fingerprint_file(path):
    return acoustid.fingerprint_file(path)


def acoustid_lookup(fingerprint, duration):
    return acoustid.lookup(ACOUSTID_API_KEY, fingerprint, duration)


def get_recordingids_for_file(filepath):
    res = acoustid.match(ACOUSTID_API_KEY, filepath)
    if res is None:
        return []
    return [mid for score, mid, title, artist_name in res]
