# **Hotkey Panels** Add-on

## Aperçu

Hotkey Panels est un add-on conçu pour optimiser votre workflow dans Blender en vous permettant d’afficher, sous forme de menus contextuels (pop-up), les panneaux des add-ons installés.

Il détecte automatiquement ces panneaux et offre la possibilité de créer des raccourcis pour accéder rapidement à vos fonctionnalités préférées, sans avoir à chercher sans cesse dans la sidebar. Vous gagnez ainsi un temps précieux et profitez d’une meilleure organisation de vos outils.

> **Note** : Seule la version expérimentale est proposée ici ; elle peut présenter des problèmes de compatibilité et de fiabilité. Il est donc recommandé de l’utiliser sur des projets non critiques ou de sauvegarder régulièrement vos fichiers.

> **Important** : Si certains add-ons n’intègrent pas le code nécessaire pour être gérés par Hotkey Panels, je ne peux malheureusement pas y remédier.

> Certains panneaux ne sont visibles que si les conditions de leur add-on d’origine sont remplies (par exemple, avoir un objet spécifique sélectionné, être en mode Édition, posséder une armature, etc.). Si un panneau censé s’afficher ne se montre pas, pensez à vérifier que ces conditions sont bien remplies dans votre scène.

---

## Installation

1. **Téléchargez l’add-on** (fichier `.py`).
2. Ouvrez Blender, puis rendez-vous dans **`Edit > Preferences > Add-ons`**.
3. Cliquez sur **`Install`** et sélectionnez le fichier `.py` téléchargé.
4. Validez ensuite l’activation du plug-in dans la liste des add-ons.

---

## Principales Fonctionnalités

- **Raccourcis Clavier Personnalisés**  
  Assignez des touches (ou combinaisons de touches) pour déclencher instantanément l’affichage de vos panneaux extraits de vos add-ons favoris.

- **Gestion Flexible des Raccourcis**  
  Activez/désactivez un raccourci en un clic dans les préférences de l’add-on. Vous pouvez également dupliquer ou supprimer facilement un raccourci.

- **Organisation Automatique des Panneaux**  
  Les panneaux sont classés selon l’add-on dont ils proviennent, ce qui facilite leur sélection (basé sur le `bl_category` ou le HEADER de chaque add-on).

- **Icones et Noms Personnalisables**  
  Donnez à chaque panneau un nom et une icône afin de l’identifier plus rapidement.

- **Import/Export des Raccourcis**  
  Permet de copier la configuration d’un Hotkey Panel dans le presse-papier, puis de l’importer en un clic, que ce soit dans un autre Hotkey Panel ou sur une autre version de Blender.  
  Sauvegardez ainsi votre configuration ou partagez-la facilement avec d’autres utilisateurs.

---

## Modes d’Affichage des Panneaux

### Standard (Stable)
Affiche un menu contextuel traditionnel lorsque vous utilisez le raccourci. Vous choisissez ensuite le panneau désiré parmi ceux associés.

### Pop-up (Expérimental)
Affiche directement les panneaux sous forme de menu pop-up, positionnés selon les réglages définis pour chaque panneau dans le Hotkey panel correspondant.

> **Note** : Cette fonctionnalité est expérimentale et peut présenter des problèmes de stabilité et de compatibilité selon la configuration et la version de Blender.  
> Elle fonctionne généralement sans trop de bugs sur les versions antérieures à la 3.6 (notamment 3.5), mais peut être instable à partir de Blender 3.6 et au-dessus.

### Pie Menu (Stable)
Présente un menu circulaire regroupant plusieurs panneaux. Idéal pour naviguer rapidement entre diverses catégories, avec un système de pagination si vous avez plus de panneaux que ne peut en contenir un seul cercle.

---

## Utilisation Rapide

1. Dans les **Préférences de l’add-on**, créez un nouveau raccourci en cliquant sur **“Add Hotkey Panel”**.
2. Sélectionnez les touches (par exemple, `Q`, avec ou sans `Ctrl/Alt/Shift`).
3. Choisissez le **Mode d’Exécution** parmi :  
   - **Standard**  
   - **Pop Up**  
   - **Pie Menu**
4. Sélectionnez un ou plusieurs panneaux à associer au raccourci, puis personnalisez au besoin leurs noms, icônes ou marges (si vous utilisez le **Pop Up**).
5. Quittez les préférences et testez le raccourci dans la Vue 3D.

---

## Points Importants et Limitations

> **Note** : Seule la version expérimentale est proposée ici ; elle peut présenter des problèmes de compatibilité et de fiabilité. Il est donc recommandé de l’utiliser sur des projets non critiques ou de sauvegarder régulièrement vos fichiers.

> **Important** : Si certains add-ons n’intègrent pas le code nécessaire pour être gérés par Hotkey Panels, je ne peux malheureusement pas y remédier.

> Certains panneaux ne sont visibles que si les conditions de leur add-on d’origine sont remplies (par exemple, avoir un objet spécifique sélectionné, être en mode Édition, posséder une armature, etc.). Si un panneau censé s’afficher ne se montre pas, pensez à vérifier que ces conditions sont bien remplies dans votre scène.

> **Note** : Cette fonctionnalité est expérimentale et peut présenter des problèmes de stabilité et de compatibilité selon la configuration et la version de Blender.

> Elle fonctionne généralement sans trop de bugs sur les versions antérieures à la 3.6 (notamment 3.5), mais peut être instable à partir de Blender 3.6 et au-dessus.

---

## Support et Communauté

- **Forum Blender Artists** : Partagez vos retours ou vos rapports de bug sur le [sujet dédié](https://blenderartists.org/t/hotkey-panels-feedback/1542369?u=soee).
- **Tutoriels Vidéo** : Consultez les vidéos YouTube (lien à venir) pour une démonstration pas à pas.
- **Autres Liens** : Retrouvez toutes les ressources officielles et liens utiles sur mon [Linktree].

---

N’hésitez pas à partager vos retours et à signaler d’éventuels problèmes. Grâce à vos retours, l’add-on continuera d’évoluer et de gagner en stabilité.

---

**Créé par** : Soee  
**Version** : 2.5 (Expérimentale)  
**Licence** : Communautaire  
