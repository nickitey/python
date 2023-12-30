from xml.etree.ElementTree import XMLParser

# Вам дано описание пирамиды из кубиков в формате XML. Кубики могут быть трех цветов: красный(red),
# зеленый(green) и синий(blue). Для каждого кубика известны его цвет, и известны кубики,
# расположенные прямо под ним.
# Пример:
# <cube color="blue">
#  <cube color="red">
#    <cube color="green">
#    </cube>
#  </cube>
#  <cube color="red">
#  </cube>
# </cube>

# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
# имеют ценность 3. И т.д.
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.


xml_color = ('<cube color="blue">'
             '<cube color="red">'
             '<cube color="green">'
             '</cube>'
             '</cube>'
             '<cube color="red">'
             '</cube>'
             '</cube>')


class CountDepth:  # The target object of the parser
    depth = 0
    colors_count = {'red': 0,
                    'green': 0,
                    'blue': 0
                    }

    def start(self, tag, attrib):  # Called for each opening tag.
        self.depth += 1
        if attrib['color'] == 'red':
            self.colors_count['red'] += self.depth
        elif attrib['color'] == 'green':
            self.colors_count['green'] += self.depth
        else:
            self.colors_count['blue'] += self.depth

    def end(self, tag):  # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass  # We do not need to do anything with data.

    def close(self):  # Called when all data has been parsed.
        return self.colors_count


def count_xml_color_cubes(string_xml):
    target = CountDepth()
    parser = XMLParser(target=target)
    parser.feed(string_xml)
    return parser.close()


assert count_xml_color_cubes(xml_color) == {'red': 4, 'green': 3, 'blue': 1}
print('Pass')
