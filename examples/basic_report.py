import matplotlib.pyplot as plt
from repen import Report

if __name__ == "__main__":
    basic_report = Report(title="TEST", debug=True)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])

    basic_report.add("# Lorem Ipsum").add(
        """
# **Complete** Markdown ++*Demo*++

**Bold text** with *italic inside* and ~~strikethrough~~.  
***Triple*** formatting shows **bold *and italic***.

`Code blocks` ignore **formatting**: `print("**Hello**")` prints literally.

## **Nesting** Examples

**Outer bold with *inner italic* and ~~strikethrough~~**. ***All three*** ++combined++.

### **Edge** Cases

**Bold ends **here** and new bold starts**. *Same for *italic**.

 ~~Invalid ~~crossing~~ but handled~~.

**Final *sentence* with `code` and ~~formatting~~.**
        """
    ).add(fig)

    basic_report.save("test.html")
