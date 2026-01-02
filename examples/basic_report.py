import matplotlib.pyplot as plt
from PIL import Image as PILImage
from repen import Report

if __name__ == "__main__":
    basic_report = Report(title="TEST", debug=True)

    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [4, 5, 6])

    with open("/home/kartiz0l/downloads/9.jpg", "rb") as f:
        image_content = f.read()

    im = PILImage.open("/home/kartiz0l/downloads/image.jpeg")

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
    ).add(("/home/kartiz0l/downloads/2025-12-22-134856_hyprshot.png", "TEST")).add(
        image_content
    ).add(
        im
    )

    basic_report.add(
        (
            fig,
            "**Lorem Ipsum** is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
        )
    )

    basic_report.save("test.html")
