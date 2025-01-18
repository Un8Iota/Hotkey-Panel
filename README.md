# Hotkey Panels

---

# **Eng** **Hotkey Panels** Add-on – Experimental Version

## Overview

Hotkey Panels is an add-on designed to optimize your workflow in Blender by allowing you to display installed add-on panels in contextual (pop-up) menus.

It automatically detects these panels and enables you to create shortcuts for quick access to your favorite features, without constantly searching through the sidebar. This saves you valuable time and provides a more organized workspace.

> **Note**: Only the experimental version is available here, which may lead to compatibility or stability issues. It is therefore recommended for non-critical projects or to ensure regular backups.
>
> **Important**: If some add-ons do not include the code required to be handled by Hotkey Panels, I unfortunately cannot fix that.
>
> Some panels are only visible if the conditions set by their original add-on are met (for example, having a specific object selected, being in Edit mode, having an armature, etc.). If a panel that should appear is not showing, please check that you have met all those conditions in your scene.

---

## Installation

1. **Download the add-on** (the `.py` file).
2. Open Blender, then go to **`Edit > Preferences > Add-ons`**.
3. Click **`Install`** and select the `.py` file you downloaded.
4. Finally, enable the plugin in the Add-ons list.

---

## Main Features

- **Custom Keyboard Shortcuts**  
  Assign keys (or key combinations) to instantly display panels from your preferred add-ons.

- **Flexible Shortcut Management**  
  Enable or disable a shortcut with a single click in the add-on preferences. You can also easily duplicate or remove a shortcut.

- **Automatic Panel Organization**  
  Panels are categorized by the add-on they come from, making them easier to find (using the HEADER each add-on provides).

- **Custom Icons and Names**  
  Give each panel a unique name and icon to identify it more quickly.

- **Shortcut Import/Export**  
  Allows you to copy a Hotkey Panel’s configuration to your clipboard, then import it with a single click—whether in another Hotkey Panel or on another version of Blender.  
  Easily save or share your configuration with other users.

---

## Panel Display Modes

- **Standard (Stable)**  
  Displays a traditional context menu when using the shortcut. You then select which panel to open from those associated.

- **Pop-up (Experimental)**  
  Immediately shows panels in a pop-up menu, positioned according to the settings defined for each panel in the relevant Hotkey Panel.  
  > **Note**: This feature is experimental and may have stability or compatibility issues depending on your setup and Blender version.  
  > It generally works without too many bugs on versions prior to 3.5, but may become unstable from Blender 3.6 and above.

- **Pie Menu (Stable)**  
  Opens a circular menu that contains multiple panels. Perfect for quickly navigating between different categories, with a pagination system if you have more panels than fit into a single circle.

---

## Quick Usage

1. In the **Add-on Preferences**, create a new shortcut by clicking **“Add Hotkey Panel”**.
2. Select the keys (e.g., `Q`), optionally with `Ctrl/Alt/Shift`.
3. Choose an **Execution Mode**:  
   - **Standard**  
   - **Pop Up**  
   - **Pie Menu**
4. Select one or more panels to associate with the shortcut, and optionally customize their names, icons, or margins (if using **Pop Up**).
5. Close Preferences and test your shortcut in the 3D View.

---

## Important Notes and Limitations

> **Note**: This feature is experimental and may cause stability or compatibility issues depending on your setup and Blender version.
>
> **Note**: Only the experimental version is provided here, which may lead to compatibility or stability issues. It is recommended for non-critical projects or for regular backups.
>
> **Important**: If certain add-ons do not include the required code for Hotkey Panels, there is unfortunately nothing I can do.
>
> Some panels will only appear if the conditions from their original add-on are met (for example, an object being selected, using Edit mode, having an armature, etc.). If a panel that should appear is missing, check these conditions are satisfied in your scene.

---

## Support and Community

- **Blender Artists Forum**: Share feedback or bug reports on the [dedicated thread](https://blenderartists.org/t/hotkey-panels-feedback/1542369?u=soee).  
- **Video Tutorials**: Check upcoming YouTube videos (link to come) for a step-by-step demonstration.  
- **Other Links**: Find all official resources and links on my [Linktree].

---

Feel free to share your feedback and report any issues. Your input helps the add-on continue to evolve and become more stable.

---

**Created by**: Soee  
**Version**: 2.5 (Experimental)  
**License**: Community  

---

# **Eng** Add-on **Hotkey Panels**

## Aperçu

Hotkey Panels est un add-on conçu pour optimiser votre workflow dans Blender en vous permettant d’afficher, sous forme de menus contextuels (pop-up), les panneaux des add-ons installés.

Il détecte automatiquement ces panneaux et offre la possibilité de créer des raccourcis pour accéder rapidement à vos fonctionnalités préférées, sans avoir à chercher sans cesse dans la sidebar. Vous gagnez ainsi un temps précieux et profitez d’une meilleure organisation de vos outils.

> **Note** : Seule la version expérimentale est proposée ici ; elle peut présenter des problèmes de compatibilité et de fiabilité. Il est donc recommandé de l’utiliser sur des projets non critiques ou de sauvegarder régulièrement vos fichiers.
>
> **Important** : Si certains add-ons n’intègrent pas le code nécessaire pour être gérés par Hotkey Panels, je ne peux malheureusement pas y remédier.
>
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
  Les panneaux sont classés selon l’add-on dont ils proviennent, ce qui facilite leur sélection (basé sur le HEADER de chaque add-on).

- **Icones et Noms Personnalisables**  
  Donnez à chaque panneau un nom et une icône afin de l’identifier plus rapidement.

- **Import/Export des Raccourcis**  
  Permet de copier la configuration d’un Hotkey Panel dans le presse-papier, puis de l’importer en un clic, que ce soit dans un autre Hotkey Panel ou sur une autre version de Blender.  
  Sauvegardez ainsi votre configuration ou partagez-la facilement avec d’autres utilisateurs.

---

## Modes d’Affichage des Panneaux

- **Standard (Stable)**  
  Affiche un menu contextuel traditionnel lorsque vous utilisez le raccourci. Vous choisissez ensuite le panneau désiré parmi ceux associés.

- **Pop-up (Expérimental)**  
  Affiche directement les panneaux sous forme de menu pop-up, positionnés selon les réglages définis pour chaque panneau dans le Hotkey panel correspondant.  
  > **Note** : Cette fonctionnalité est expérimentale et peut présenter des problèmes de stabilité et de compatibilité selon la configuration et la version de Blender.  
  > Elle fonctionne généralement sans trop de bugs sur les versions antérieures à la 3.5, mais peut être instable à partir de Blender 3.6 et au-dessus.

- **Pie Menu (Stable)**  
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

> **Note** : Cette fonctionnalité est expérimentale et peut présenter des problèmes de stabilité et de compatibilité selon la configuration et la version de Blender.

> **Note** : Seule la version expérimentale est proposée ici ; elle peut présenter des problèmes de compatibilité et de fiabilité. Il est donc recommandé de l’utiliser sur des projets non critiques ou de sauvegarder régulièrement vos fichiers.

> **Important** : Si certains add-on n’intègrent pas le code nécessaire pour être gérés par Hotkey Panels, je ne peux malheureusement pas y remédier.

> Certains panneaux ne sont visibles que si les conditions de leur add-on d’origine sont remplies (par exemple, avoir un objet spécifique sélectionné, être en mode Édition, posséder une armature, etc.). Si un panneau censé s’afficher ne se montre pas, pensez à vérifier que ces conditions sont bien remplies dans votre scène.

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
