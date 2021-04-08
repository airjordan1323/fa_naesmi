from typing import Union

import aiofiles
from fastapi import UploadFile, HTTPException


async def load_image(file_name: str = None, file: UploadFile = None):
    async with aiofiles.open(file_name, "wb") as buffer:
        data = await file.read()
        await buffer.write(data)


async def filters_backends(model, limit: Union[int, None] = None, off: Union[int, None] = 0, page: Union[int, None] = None,
                     page_size: Union[int, None] = 10, ordering: Union[str, None] = None):
    if (limit and off) is not None:
        return model.limit(limit).offset(off)
    elif (page and page_size) is not None:
        return model.paginate(page, page_size)
    elif ordering is not None:
        return model.order_by(ordering)


def ultimate_view(func, *args, **kwargs):
    async def view(limit: Union[int, None] = None, off: Union[int, None] = 0, page: Union[int, None] = None,
                   page_size: Union[int, None] = 10, ordering: Union[str, None] = None):
        instance = func()
        try:
            model = instance['model'].objects
        except:
            raise HTTPException(status_code=1999, detail="Здесь нарушать правила запрещена блеать")
        if (limit and off) is not None or (page and page_size) is not None or ordering is not None:
            model = await filters_backends(model, limit=limit, off=off, page=page, page_size=page_size,
                                           ordering=ordering)
        return await model.all()

    return view




