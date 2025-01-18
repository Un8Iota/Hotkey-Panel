# Hotkey Panels

---

## **English Version**

# **Hotkey Panels** Add-on – Experimental Version

## Overview

Hotkey Panels is an add-on designed to optimize your workflow in Blender by displaying installed add-on panels in contextual (pop-up) menus.

It automatically detects these panels and allows you to create shortcuts for quick access to your preferred features, without constantly searching through the sidebar. This saves you valuable time and provides a more organized workflow.

> **Note**: Only the experimental version is offered here, which may lead to compatibility or stability issues. It is therefore recommended to use it on non-critical projects or make regular backups of your work.
>
> **Important**: If some add-ons do not include the code required to be handled by Hotkey Panels, I unfortunately cannot fix that.
>
> Certain panels are only visible if the conditions set by their original add-on are met (for example, having a specific object selected, being in Edit mode, having an armature, etc.). If a panel that should appear is not showing, make sure those conditions are met in your scene.

---

## Installation

1. **Download the add-on** (the `.py` file).
2. Open Blender and go to **`Edit > Preferences > Add-ons`**.
3. Click **`Install`** and select the `.py` file you downloaded.
4. Finally, enable the plugin in the Add-ons list.

---

## Main Features

- **Custom Keyboard Shortcuts**  
  Assign keys (or key combinations) to instantly display panels from your favorite add-ons.

- **Flexible Shortcut Management**  
  Enable or disable a shortcut in a single click within the add-on preferences. You can also duplicate or remove a shortcut easily.

- **Automatic Panel Organization**  
  Panels are organized according to the add-on they come from, making them easier to locate (using the HEADER of each add-on).

- **Custom Icons and Names**  
  Give each panel its own name and icon for quick recognition.

- **Shortcut Import/Export**  
  Lets you copy a Hotkey Panel’s configuration to your clipboard and import it with a single click—whether in another Hotkey Panel or another Blender version.  
  Save or share your settings effortlessly with other users.

---

## Panel Display Modes

- **Standard (Stable)**  
  Displays a traditional context menu when you use the shortcut. You then choose which panel to open among those associated.

- **Pop-up (Experimental)**  
  Instantly shows panels in a pop-up menu, positioned according to the settings you define for each panel in the corresponding Hotkey Panel.  
  > **Note**: This feature is experimental and can exhibit stability or compatibility issues depending on your setup and Blender version.  
  > It generally works without too many bugs on versions prior to 3.5, but may become unstable starting from Blender 3.6 and above.

- **Pie Menu (Stable)**  
  Displays a circular menu containing multiple panels. Ideal for quickly navigating between various categories, with a pagination system if you have more panels than can fit in a single circle.

---

## Quick Usage

1. In the **Add-on Preferences**, create a new shortcut by clicking **“Add Hotkey Panel”**.
2. Select the keys (for example, `Q`, with optional `Ctrl/Alt/Shift`).
3. Choose the **Execution Mode** among:
   - **Standard**
   - **Pop Up**
   - **Pie Menu**
4. Select one or more panels to associate with the shortcut, then optionally customize their names, icons, or margins (if using **Pop Up**).
5. Close the preferences and try out the shortcut in the 3D View.

---

## Important Notes and Limitations

> **Note**: This feature is experimental and may cause stability or compatibility issues depending on your setup and Blender version.

> **Note**: Only the experimental version is offered here; it may have compatibility or stability problems. It’s recommended to use it for non-critical projects or to back up your work regularly.

> **Important**: If certain add-ons do not have the necessary code to be managed by Hotkey Panels, there’s unfortunately nothing I can do about it.

> Some panels only appear if the conditions set by their original add-on are met (for instance, selecting a specific object, being in Edit mode, or having an armature, etc.). If a panel that should appear isn’t showing up, ensure that these conditions are met in your scene.

---

## Support and Community

- **Blender Artists Forum**: Share your feedback or bug reports on the [dedicated thread](https://blenderartists.org/t/hotkey-panels-feedback/1542369?u=soee).  
- **Video Tutorials**: Check out upcoming YouTube videos for a step-by-step demonstration.  
- **Other Links**: Find all official resources and links on my [Linktree].

---

Feel free to share your feedback and report any issues. Your input helps the add-on continue to evolve and become more stable.

---

**Created by**: Soee  
**Version**: 2.5 (Experimental)  
**License**: Community

---

## **Version Française**

# Add-on **Hotkey Panels** – Version Expérimentale

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
  Les panneaux sont classés selon l’add-on dont ils proviennent, ce qui facilite leur sélection (fourni avec le HEADER de chaque add-on).

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
  > Note : Cette fonctionnalité est expérimentale et peut présenter des problèmes de stabilité et de compatibilité selon la configuration et la version de Blender.  
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

> Note : Cette fonctionnalité est expérimentale et peut présenter des problèmes de stabilité et de compatibilité selon la configuration et la version de Blender.

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
