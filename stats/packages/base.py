class PackageBuilder(object):

    def render_all_objects(self, all_objects=None):
        all_rendered_object = []
        if all_objects is None:
            all_objects = self.get_objects()
        for each_object in all_objects:
            all_rendered_object.append(self.render_each_object(each_object))
        print all_rendered_object
        return ",\n".join(all_rendered_object)

    def render_all_objects_as_list(self):
        template = """[\n{0}\n]"""
        return template.format(self.render_all_objects())