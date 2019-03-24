#Voice Parser 2.0

import os, re

numFiles = 0
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.rpy'):
            inputFilePath = os.path.join(root, file)
            outputFilePath = os.path.join(root, file)
            #outputFilePath = os.path.join(root, 'parsed_'+file)
            nums = re.findall(r'\d+', file)
            routeTag = '00'
            if len(nums) > 0:
                routeTag = nums[0]

            with open(inputFilePath, 'r') as infile:
                lineCount = 1
                sceneNumber = 'default'

                found = False
                outstr = ""
                for line in infile:
                    trimmedLine = line.strip().strip('\t')
                    if trimmedLine.startswith('label '):
                        sceneNumber = trimmedLine.split()[1].strip(':')

                    if trimmedLine.startswith('che'):
                        found = True
                        leadingWhitespace = line.split('che')[0]
                        outstr += leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Cheshire (shiena)\n'
                        lineCount += 1
                    elif 'min' in trimmedLine[:2]:
                        found = True
                        leadingWhitespace = line.split('min')[0]
                        outstr += leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Ji-min ()\n'
                        lineCount += 1
                    elif 'bos' in trimmedLine[:3]:
                        found = True
                        leadingWhitespace = line.split('bos')[0]
                        outstr += leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Boss ()\n'
                        lineCount += 1
                    elif 'mom' in trimmedLine[:3]:
                        found = True
                        leadingWhitespace = line.split('mom')[0]
                        outstr += leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Mom ()\n'
                        lineCount += 1
                    elif 'dad' in trimmedLine[:3]:
                        found = True
                        leadingWhitespace = line.split('dad')[0]
                        outstr += leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Dad ()\n'
                        lineCount += 1
                    elif 'caf' in trimmedLine[:3]:
                        found = True
                        leadingWhitespace = line.split('caf')[0]
                        outstr += leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Cafe Owner ()\n'
                        lineCount += 1
                    elif 'vm' in trimmedLine[:3]:
                        found = True
                        leadingWhitespace = line.split('vm')[0]
                        outstr += leadingWhitespace + 'voice "' + routeTag + '-' + sceneNumber + '-' + str(lineCount) + '.mp3" #Friend ()\n'
                        lineCount += 1

                    outstr += line

                if found:
                    with open(outputFilePath, 'w') as outfile:
                        outfile.write(outstr)
                        numFiles += 1

                        print '  ' + outputFilePath
print('\nNumber of files created: ' + str(numFiles))
