# with open("/Users/bmosley/Desktop/cases.txt", "r") as f:
#     # f.write(_swift_file(app, _generate_labels))
#     # print(f"\nfile written to: {_pth}")
#     lines = f.readlines()

#     r = []
#     for line in lines:
#         line = line.strip()
#         if line.startswith("return") or line.startswith("//") or not line:
#             continue
#         line = line.replace("case .", "").replace(":", "").replace(",", "")
#         r.append(line)

#     r.sort()
#     for x in r:
#         print(x)

with open("/Users/bmosley/Desktop/hi.txt", "r") as f:
    # f.write(_swift_file(app, _generate_labels))
    # print(f"\nfile written to: {_pth}")
    lines = f.readlines()

    r = []
    for line in lines:
        line = line.strip()
        # print(f"""static let {line} = appendPrefixWith("{line}")""")
        if "UIA.TV.Tabs" in line:
            line = line.split("UIA.TV.Tabs.")[1].strip().split("'")[0]
            print(line)
