def parse_index(file_stream):
    lines = [l.replace("\n", "") for l in file_stream.readlines()]
    index = []
    try:
        for l in lines:
            components = l.split(",")
            rdi = IndexEntry()
            rdi.filename = components[0]
            rdi.cached_name = components[1]
            rdi.md5_checksum = components[2]
            rdi.size_in_bytes = int(components[3])
            if len(components) > 4:
                rdi.compressed_size = int(components[4])
            else:
                rdi.compressed_size = 0

            index.append(rdi)

    except Exception:
        raise ValueError("Bad index file")

    return index


class IndexEntry(object):
    def __init__(self):
        self.filename = ""
        self.cached_name = ""
        self.md5_checksum = ""
        self.size_in_bytes = 0
        self.compressed_size = 0
    def __hash__(self):
        return hash(self.cached_name)
    def __eq__(self, other):
        return self.cached_name == other.cached_name