# Hotkey-Panel

# Add-on **Hotkey Panels** – Version Expérimentale

## Aperçu

L’add-on **Hotkey Panels** pour Blender vous permet d’assigner des raccourcis clavier personnalisés afin d’ouvrir rapidement des panneaux spécifiques provenant de vos add-ons installés. Cette version est **expérimentale**, ce qui signifie qu’elle inclut des fonctionnalités avancées (comme l’activation directe des panneaux ou le réglage des marges), mais qu’elle peut aussi comporter des instabilités ou des bugs connus.

> **Note** : Comme seule la version expérimentale est fournie ici, il est possible que vous rencontriez des problèmes de compatibilité ou de fiabilité. Utilisez-la de préférence sur des projets non critiques ou faites des sauvegardes régulières de vos scènes.

---

## Principales Fonctionnalités

- **Raccourcis Clavier Personnalisés**  
  Assignez des touches (ou combinaisons de touches) pour déclencher instantanément l’affichage de vos panneaux favoris.

- **Gestion Flexible des Raccourcis**  
  Activez/désactivez un raccourci en un clic dans les préférences de l’add-on. Vous pouvez également dupliquer ou supprimer facilement un raccourci.

- **Organisation Automatique des Panneaux**  
  Les panneaux sont classés selon l’add-on dont ils proviennent, ce qui facilite leur sélection.

- **Icones et Noms Personnalisables**  
  Donnez à chaque panneau un nom et une icône afin de l’identifier plus rapidement.

- **Import/Export des Raccourcis**  
  Sauvegardez votre configuration ou partagez-la avec d’autres utilisateurs en un clic. Importez les fichiers de configuration d’autres personnes pour gagner du temps.

### Fonctionnalités Expérimentales Incluses

- **Activation Directe (Pop-Up)**  
  Permet d’afficher instantanément certains panneaux sous le curseur de la souris, sans passer par un menu contextuel.  
  - *Réglage de la Vitesse de la Souris* : Ajustez la vitesse de déplacement de la souris pour rendre la transition plus fluide.  
  - *Réglage des Marges (Padding)* : Affinez le positionnement horizontal et vertical des panneaux appelés grâce à des paramètres de “padding”.

- **Menu Circulaire (Pie Menu)**  
  Activez plusieurs panneaux via un menu circulaire, idéal pour regrouper différentes fonctionnalités sur un même raccourci. Feuilletez facilement plusieurs “pages” de panneaux s’il y en a trop à afficher sur un seul écran.

> **Attention** : Ces fonctionnalités avancées peuvent parfois présenter des comportements imprévisibles ou ne pas fonctionner correctement sur certaines configurations ou versions de Blender (notamment à partir de la 3.5).

---

## Installation

1. **Téléchargez l’add-on** (fichier `.py`).
2. Ouvrez Blender, puis rendez-vous dans **`Edit > Preferences > Add-ons`**.
3. Cliquez sur **`Install`** et sélectionnez le fichier `.py` téléchargé.
4. Validez ensuite l’activation du plug-in dans la liste des add-ons.

---

## Utilisation Rapide

1. Dans les **Préférences de l’add-on**, créez un nouveau raccourci en cliquant sur **“Add Hotkey Panel”**.  
2. Donnez-lui un nom et sélectionnez les touches (par exemple, `Q`, avec ou sans `Ctrl/Alt/Shift`).  
3. Choisissez le **Mode d’Exécution** parmi :  
   - **Standard** : Ouvre un menu contextuel simple.  
   - **Pop Up** (Expérimentale) : Affiche directement le panneau sous le curseur.  
   - **Pie Menu** (Expérimentale) : Menu circulaire pratique pour regrouper plusieurs panneaux.  
4. Sélectionnez un ou plusieurs panneaux à associer au raccourci, puis personnalisez au besoin leurs noms, icônes ou marges (si vous utilisez le **Pop Up**).  
5. Quittez les préférences et testez le raccourci dans la Vue 3D.

---

## Exemples d’Actions

- **Raccourci en Pop-Up (Activation Directe)**  
  Attribuez la touche `Q` pour ouvrir instantanément un panneau d’options de modélisation sous le curseur.  
  Vous pouvez ensuite régler la marge (X/Y) pour que le panneau apparaisse pile où vous le souhaitez.

- **Menu Circulaire (Pie Menu)**  
  Avec `Alt + M`, ouvrez un menu circulaire regroupant divers panneaux de texturing. Passez d’une “page” à l’autre en cliquant sur “Next/Previous Page” pour accéder à un ensemble plus large de panneaux.

---

## Points Importants et Limitations

- **Compatibilité avec Blender 3.5+** : Certains utilisateurs signalent des soucis pour afficher les panneaux sous certaines versions récentes.  
- **Enregistrement des Panneaux** : Certains panneaux d’add-ons tiers peuvent ne pas être reconnus ou s’afficher de manière incomplète.  
- **Réglage de la Vitesse de la Souris** : Selon la scène ou la configuration, le réglage peut parfois ne pas s’appliquer correctement.  
- **Marge des Panneaux (Padding)** : Les ajustements de position peuvent varier selon le système d’exploitation ou la version de Blender.

---

## Support et Communauté

- **Forum Blender Artists** : Partagez vos retours ou vos rapports de bug sur le [sujet dédié](https://blenderartists.org/t/hotkey-panels-feedback/1542369?u=soee).  
- **Tutoriels Vidéo** : Consultez les vidéos YouTube (lien à venir) pour une démonstration pas à pas.  
- **Autres Liens** : Retrouvez toutes les ressources officielles et liens utiles sur mon [Linktree].

---

## Conclusion

La version expérimentale de l’add-on **Hotkey Panels** peut grandement accélérer votre workflow grâce à un accès ultra rapide à vos panneaux préférés. Malgré quelques risques de bugs, ses fonctionnalités innovantes (Pop-Up direct, Pie Menu, padding ajustable) ouvrent de nouvelles possibilités d’organisation et d’ergonomie dans Blender.

N’hésitez pas à partager vos retours et à signaler d’éventuels problèmes. Grâce à vos retours, l’add-on continuera d’évoluer et de gagner en stabilité.

---

**Créé par** : Soee  
**Version** : 2.5 (Expérimentale)  
**Licence** : Communautaire  
**Lien de téléchargement** : [À insérer]
