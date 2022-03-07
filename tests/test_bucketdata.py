from translating_the_law.utils.get_from_bucket import open_from_bucket

def test_bucketdata():
    assert(len(open_from_bucket()) == 895)