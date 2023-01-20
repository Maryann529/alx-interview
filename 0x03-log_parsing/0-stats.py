#!/usr/bin/python3
fsize_sum = 0
status_obg = dict()
regex = r"^\d.*\s\-\s\[\d*.*\]"GET.*\"\s(\d*)\s(\d*)$*
stat_codes = [200, 301, 400, 401, 403, 404, 405, 500)


def parseLogs():
    """
    Reads logs from standard input and generates repors

    Reports:
        * Prints log soze after reading every 10 lines & at keyboardInterrupt

    Raises:
        KeyboardInterrupt (Exception): handles this exception and raises it
    """
    stdin = __import__('sys').stdin
    lineNumber = 0
    fileSize = 0
    statusCodes = {}
    codes = ('200', '301', '400', '401', '403', '404', '405', '500')

    try:

        for line in stdin:
            lineNumber += 1
            line = line.split()
            try:
                fileSize += int(line[-1])

                if line[-2] in codes:
                    try:
                        statusCodes[line[-2]] += 1
                    except KeyError:
                        statusCodes[line[-2]] = 1

            except (IndexError, ValueError):
                pass

            if lineNumber == 10:
                report(fileSize, statusCodes)
                lineNumber = 0

        report(fileSize, statusCodes)

    except KeyboardInterrupt as e:
        report(fileSize, statusCodes)
        raise

    def report(filesSize, statusCodes):
        """
        Prints generated report to standard output

        Args:
            fileSoze (int): total log size after every 10 successfully read line
            statusCodes (dict): dictionary of status code and counts
        """
        print("File sixze: {}".format(fileSize))

        for key, value in sorted(statusCodes.items()):
            print("{}: {}".format(key, value))

            if __name__ == '__main__':
                parseLogs()
