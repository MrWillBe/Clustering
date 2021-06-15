from barycenter_list import Barycenter_List
from barycenter import Barycenter

class Operator:
    pass

    # return [Norme(1), ..., Norme(n)]
    def norme(barycenters: Barycenter_List, x, y):
        # Liste retournée à la fin
        normes = []
        # Variable qui contient les coordonnées du point en paramètre
        point = [x, y]
        # Liste de barycentres
        barycenter_list = barycenters.barycenter_list
        # Calcul de la norme du point A(x,y) par rapport aux n barycentres
        for i in range(len(barycenter_list)):
            barycentre = barycenter_list[i].getcoord()
            norme_i = (point[0] - barycentre[0]) ** 2 + (point[1] - barycentre[1]) ** 2
            normes.append(norme_i)
        return normes

    def attribuer(normes_list):
        # Tableau contenant "n" clusters
        clusters = [[] for i in range(len(normes_list[0]))]
        # Déterminer la plus petite norme de chaque point et les attribuer au cluster correspondant
        # Nombre de lignes
        for i in range(len(normes_list)):
            # Valeur minimale parmi les "n" normes
            minimum = min(normes_list[i])
            # Index de la valeur minimale
            index_min = normes_list[i].index(minimum)
            # Ajout du point dans le cluster correspondant
            clusters[index_min].append(i)
        return clusters

    def average(clusters, data, barycenter_list):
        barycenter_new = []
        # Accéder aux "n" clusters
        for i in range(len(clusters)):
            sum_abs = 0
            sum_ord = 0
            # Accéder aux éléments du cluster
            for j in range(len(clusters[i])):
                # Récupérer nom du point (son indice)
                point = clusters[i][j]
                # Ajouter sa coordonnée x à la somme des abscisses du cluster
                sum_abs += data.item((0,point))
                # Ajouter sa coordonnée y à la somme des ordonnées du cluster
                sum_ord += data.item((1,point))
            # Calcul de la somme des abscisses et ordonnées
            if (len(clusters[i]) != 0):
                abs_average = sum_abs / len(clusters[i])
                ord_average = sum_ord / len(clusters[i])
                barycenter_new.append(Barycenter(abs_average, ord_average))
            else:
                barycenter_new.append(barycenter_list.barycenter_list[i])

            blist_new = Barycenter_List(len(clusters))
            blist_new.barycenter_list = barycenter_new
        return blist_new, barycenter_list


    def end(barycenter_old, barycenter_list):
        for i in range(len(barycenter_list.barycenter_list)):
            for j in range(len(barycenter_list.barycenter_list[0].getcoord())):
                if( abs(barycenter_list.barycenter_list[i].getcoord()[j]-barycenter_old.barycenter_list[i].getcoord()[j]) >0.0000001 ):
                    return False
        return True


