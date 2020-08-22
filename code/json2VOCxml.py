# --------------------------------------------------------
# Written by JianFeng Liu, based on python
# json file transform to xml file automatically
# --------------------------------------------------------
import xmltodict
import json
import os

# json to xml
def jsonToXml(json_str):
    try:
        xml_str=""
        xml_str = xmltodict.unparse(json_str, pretty=1)
    except:
        xml_str = xmltodict.unparse({'request': json_str}, encoding='utf-8')
    finally:
        return xml_str

def json_to_xml(json_path,xml_path):
    if(os.path.exists(xml_path)==False):
        os.makedirs(xml_path)
    dir = os.listdir(json_path)
    for file in dir:
        print(os.path.join(json_path,file))
        file_list=file.split(".")
        # print('file_list: ',file_list,end="\n\n")
        with open(os.path.join(json_path,file), 'r') as load_f:
            # print(load_f)
            load_dict = json.load(load_f)
        # json_result = jsonToXml(load_dict)img_num        # print(type(load_dict[img_num]))
        print(len(load_dict))
        for img_num in range(len(load_dict)):
            print("第",img_num+1,"个")
            load_dict[img_num]['folder'] = 'VOC2012'
            load_dict[img_num]['filename'] = load_dict[img_num]['img_name']
            del load_dict[img_num]['img_name']
            load_dict[img_num]['source'] = {"database":"The VOC2007 Database", "annotation":"PASCAL VOC2007", "image":"flickr"}
            load_dict[img_num]['size'] = {"width":400, "height":600, "depth":3}
            load_dict[img_num]['segmented'] = 0
            load_dict[img_num]['object'] = load_dict[img_num]['items']
            del load_dict[img_num]['items']
            i = 0
            dels = []
            for object_ in load_dict[img_num]['object']:
                if object_['category']=='bk' or object_['category']=='face' or object_['category']=='hair' or object_['category']=='skin':
                    dels.append(i)
                object_['name'] = object_['category']
                del object_['category']
                object_['pose'] = 'Unspecified'
                object_['truncated'] = 0
                object_['difficult'] = 0
                object_['bndbox'] = object_['bbox']
                del object_['bbox']
                xmin = object_['bndbox']['xmin']
                ymin = object_['bndbox']['ymin']
                xmax = object_['bndbox']['xmax']
                ymax = object_['bndbox']['ymax']
                del object_['bndbox']['xmin'], object_['bndbox']['ymin'], object_['bndbox']['xmax'], object_['bndbox']['ymax']
                object_['bndbox']['xmin'] = xmin
                object_['bndbox']['ymin'] = ymin
                object_['bndbox']['xmax'] = xmax
                object_['bndbox']['ymax'] = ymax
                i += 1
            # 倒序删除
            for per_del in reversed(dels):
                # print("有没有 ",per_del,load_dict[img_num]['object'][per_del]['name'])
                load_dict[img_num]['object'].pop(per_del)
                
            json_result = xmltodict.unparse({"annotation":load_dict[img_num]})
            json_result = json_result[39:]
            # print(json_result)
            f = open(os.path.join(xml_path,load_dict[img_num]['filename'].split(".")[0]+".xml"), 'w', encoding="UTF-8")
            f.write(json_result)
            f.close()

if __name__ == '__main__':

    json_path=r"C:\Users\ASUS\Desktop\json"  #该目录为存放json文件的路径  ps:目录中只能存放json文件
    xml_path=r"C:\Users\ASUS\Desktop\xml"   #该目录为放xml文件的路径
    json_to_xml(json_path,xml_path)