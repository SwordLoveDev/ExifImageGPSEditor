from PIL import Image
import piexif

def dec_sexa(nb):
    nb = abs(nb)
    degres = int(nb)
    minutes = (nb-degres)*60
    secondes = (minutes-int(minutes))*60
    coordonnees = (degres,int(minutes),int(secondes))
    return(coordonnees)

def ordCoord(lat,long):
    liste1 = dec_sexa(lat)   
    if lat<0:
        latitude = (b'S',((liste1[0],1),(liste1[1],1),(liste1[2],1)))
    else:
        latitude = (b'N',((liste1[0],1),(liste1[1],1),(liste1[2],1)))
    
    liste2 = dec_sexa(long)
    
    if long<0:
        longitude = (b'W',((liste2[0],1),(liste2[1],1),(liste2[2],1)))
    else:
        longitude = (b'E',((liste2[0],1),(liste2[1],1),(liste2[2],1)))
    
    return((latitude, longitude))

def main():
    image = input("Le nom de l'image : ")
    monImage = Image.open(image)
    exif_dico = piexif.load(monImage.info["exif"])

    longi = float(input("Nouvelle longitude : "))
    lati = float(input("Nouvelle latitude : "))
    newCoord = ordCoord(longi, lati)
    
    exif_dico['GPS'][1] = newCoord[1][0]
    exif_dico['GPS'][2] = newCoord[0][1]
    exif_dico['GPS'][3] = newCoord[1][0]
    exif_dico['GPS'][4] = newCoord[1][1]
    
    exif_bytes = piexif.dump(exif_dico)
    monImage.save('out.jpg', "jpeg", exif = exif_bytes)
    print("Modification appliquer, nom de la nouvelle image : out.jpg")	
    
main()

