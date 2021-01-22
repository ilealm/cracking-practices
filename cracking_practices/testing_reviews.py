








def blur(height, width, image):
    for i in range(height):
        for j in range(width):
            counter = 0
            # 1 row above
            if i > 0:
                # top left
                if j > 0:
                    print(image[i - 1][j - 1])
                    counter += 1
                # top middle
                print(image[i - 1][j])
                counter += 1
                # top right
                if j < width - 1:
                    print(image[i - 1][j + 1])
                    counter += 1

            # current row, left
            if j > 0:
                print(image[i][j - 1])
                counter += 1
            # current possition
            print(image[i][j])
            counter += 1
            # current row, right
            if j < width - 1:
                print(image[i][j + 1])
                counter += 1

            # 1 row below
            if i < height - 1:
                # bottom left
                if j > 0:
                    print(image[i + 1][j - 1])
                    counter += 1
                # bottom middle
                print(image[i + 1][j])
                counter += 1
                # bottom left
                if j < width -1:
                    print(image[i + 1][j + 1])
                    counter += 1

            print(" ------ counter: ", counter)
            print()
            print()
            print()

        print("********************  end row ", i)




if __name__ == "__main__":
    image = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]  ]

    blur(4,4, image)
