from repen import Report

if __name__ == "__main__":
    basic_report = Report("TEST")

    # basic_report.add(text, chart1, char2)

    basic_report.save("test.html")

    print("HERE")
