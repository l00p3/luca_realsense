from pathlib import Path
import typer
import cv2
from rosbags.highlevel import AnyReader
from rosbags.image import message_to_cvimage
from tqdm import trange, tqdm
import os


def main(
    bag_folder: Path = typer.Argument(
        ...,
        help="Path to the folder containing the bag metadata and .db3 file.",
        show_default=False,
    ),
    output_folder: Path = typer.Argument(..., help="Folder where to save the images."),
    show_default=False,
):

    rgb_output_folder = output_folder / "rgb"
    depth_output_folder = output_folder / "depth"

    rgb_output_folder.mkdir(parents=True, exist_ok=True)
    depth_output_folder.mkdir(parents=True, exist_ok=True)

    rgb_filenames = set()
    depth_filenames = set()

    with AnyReader([Path(bag_folder)]) as reader:
        # topic and msgtype information is available on .connections list
        print("\nExtracting images")
        for connection, timestamp, rawdata in tqdm(
            reader.messages(), unit=" messages", dynamic_ncols=True
        ):
            if connection.topic == "/camera/camera/color/image_raw":
                msg = reader.deserialize(rawdata, connection.msgtype)
                img = message_to_cvimage(msg, "bgr8")
                img_filename = (
                    str(msg.header.stamp.sec)
                    + str(msg.header.stamp.nanosec).zfill(9)
                    + ".png"
                )
                cv2.imwrite(str(rgb_output_folder / img_filename), img)
                rgb_filenames.add(img_filename)
            if connection.topic == "/camera/camera/aligned_depth_to_color/image_raw":
                msg = reader.deserialize(rawdata, connection.msgtype)
                img = message_to_cvimage(msg, "mono16")
                img_filename = (
                    str(msg.header.stamp.sec)
                    + str(msg.header.stamp.nanosec).zfill(9)
                    + ".png"
                )
                cv2.imwrite(str(depth_output_folder / img_filename), img)
                depth_filenames.add(img_filename)

    rgb_imgs_to_delete = list(rgb_filenames - depth_filenames)
    depth_imgs_to_delete = list(depth_filenames - rgb_filenames)
    print("\nRemoving RGB images with no corresponding DEPTH image")
    for rgb_img in tqdm(rgb_imgs_to_delete, unit="i mages", dynamic_ncols=True):
        os.remove(str(rgb_output_folder / rgb_img))
    print("\nRemoving DEPTH images with no corresponding RGB image")
    for depth_img in tqdm(depth_imgs_to_delete, unit=" images", dynamic_ncols=True):
        os.remove(str(depth_output_folder / depth_img))


if __name__ == "__main__":
    typer.run(main)
