import math


class CountVectorizer:
      def __init__(self):
        '''
        класс, предназначенный для анализа текстов
        '''
        self._unique_words = []
      def fit_transform(self, data):
        '''
        метод, прнимающий список слов, разделённых пробелами
        и возвращающий терм-документную матрицу
        '''
        assert type(data) is list, 'Данные должны быть переданы списком!'
        all_words = []
        for row in data:
          assert type(row) is str, 'Предложения должны быть строками!'
          all_words += [word.lower() for word in row.split()]
        self._unique_words = list(set(all_words))
        n, m = len(data), len(self._unique_words)
        count_matrix = [[0] * m for _ in range(n)]
        for ind, row in enumerate(data):
          for word in row.split():
            word = word.lower()
            number = self._unique_words.index(word)
            count_matrix[ind][number] += 1
        return count_matrix

      def get_feature_names(self):
        '''
        метод, возвращающий список слов
        '''
        if self._unique_words:
          return self._unique_words
        else:
          print('сначала вызовите метод "fit_transform"')


def fit_transform(count_matrix):
  tf_matrix = []
  for numbers_row in count_matrix:
    numbers_of_word = sum(numbers_row)
    tf_matrix_row = [round(i / numbers_of_word, 3) for i in numbers_row]
    tf_matrix.append(tf_matrix_row)

  return tf_matrix

def idf_transform(count_matrix):
  result = []
  document_count = len(count_matrix) + 1

  for col in range(len(count_matrix[0])):
    current_sum = 0
    for row in range(len(count_matrix)):
      current_sum += bool(count_matrix[row][col])
    result.append(current_sum + 1)

  for i in range(len(result)):
    result[i] = math.log(document_count / result[i]) + 1

  return result

class TfIdfTransformer():
  def fit_transform(self, matrix):
    tf = fit_transform(matrix)
    idf = idf_transform(matrix)

    tf_idf = []
    for text in tf:
      tf_idf.append([round(a * b, 3) for a, b in zip(text, idf)])
    return tf_idf

class TfIdfVectorizer(CountVectorizer):
  def __init__(self):
    super().__init__()
    self.tf_tfidf_transformer = TfIdfTransformer()

  def fit_transform(self, corpus):
    print(type(self))
    count_matrix = super().fit_transform(corpus)
    print(5)
    return self.tf_tfidf_transformer.fit_transform(count_matrix)



