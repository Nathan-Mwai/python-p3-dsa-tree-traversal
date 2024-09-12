class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    output = []
    output.append(self.root)
    while output:
      node = output.pop()
      if node['id'] == id:
        return node
      else:
        for child in node['children']:
          output.append(child)
    pass
