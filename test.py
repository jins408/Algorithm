import re

user_input = 'Along with data on the web increasing dramatically [ on_the_web, dongyi_kim ], hashing is becoming more and more popular as a method of approximate nearest neighbor search[ intro, duction, to, algorithms ]. Previous supervised hashing methods such as [ dongyi, kim, lovelyz ] utilized similarity/dissimilarity matrix to get semantic information. But the matrix is not easy to construct for a new dataset. Rather than to reconstruct the matrix, we proposed a straightforward CNN-based hashing method, i.e. binarilizing the activations of a fully connected layer with threshold 0 and taking the binary result as hash codes. This method achieved the best performance on CIFAR-10 and was comparable with the state-of-the-art on MNIST [ so_death, aaaa ]. And our experiments on CIFAR-10 suggested by [ a, aa, aaaa ] that the signs of activations may carry more information than the relative values of activations between samples, and that the co-adaption between feature extractor and hash functions is important for hashing. for more detail, see [ some_book_a, aaaa ].'

find = re.findall('\[([^]]+)\]', user_input)
words = []
result = user_input
for f in find:
    bundle = f.split(',')
    for b in bundle:
        words.append(' '+b+' ')
setWords = list(dict.fromkeys(words))

# for i in range(len(setWords)):
#     findWord = re.findall(setWords[i], result)
#     for w in findWord:
#         result = result.replace(w, str(i + 1))

wordsArr = []

for i in range(len(result)):
    if (result[i] == '['):
        for j in range(i + 2, len(result)):
            if (result[j] == ']'):
                wordsArr.append(result[i+2:j-1].split(', '))
                start = i+2
                end = j-1
                temp = result[i+2:j-1].split(', ')
                break
        #     if (result[j] != ']' and result[j] != ',' and result[j] != ' '):
        #         temp.append(result[j])
        # wordsArr.append(temp)
print(setWords)
print(wordsArr)

for i in range(len(setWords)):
    result = result.replace(setWords[i], str(i + 1))
result = result.replace('[', '[ ')
result = result.replace(']', ' ]')

a = 'asdf'
a[2] = '3'
print(a)
# for i in range(len(setWords)):
#     findWord = re.findall(setWords[i], result)
#     for w in findWord:
#         result = result.replace(w, str(i + 1))

# for a in wordsArr:
#     sortedArr = sorted(a)
#     originArr = '[ '
#     newArr = '[ '
#     for i in range(len(sortedArr)):
#         if i != len(sortedArr) - 1:
#             originArr += str(a[i]) + ', '
#             newArr += str(sortedArr[i]) + ', '
#         else:
#             originArr += str(a[i]) + ' ]'
#             newArr += str(sortedArr[i]) + ' ]'
#     result = result.replace(originArr, newArr)

for i in range(len(setWords)):
    result = result + '\n' + '[' + str(i + 1) + '] ' + setWords[i]
print(result)
